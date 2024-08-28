import os, json, pandas, argparse, sys
from collections import OrderedDict
from radon.complexity import cc_visit, cc_rank




def get_the_complexity(path, error_message):
    all_files = os.listdir(path)
    rows =  OrderedDict()
    
    for filename in all_files:
        rows[filename] = {}
        try:
            raw_script_content = open(os.path.join(path, filename),'r').read()
            script_content      = raw_script_content.replace(".None", "#.None") if filename == 'ApplyReportToWorkspace.py' else raw_script_content
            blocks = cc_visit(script_content)
            def_result_dict = {}
            for block in blocks:
                def_result_dict[block.name] = {"complexity_value": block.complexity, "complexity_rank":cc_rank(block.complexity)}
            rows[filename].update(def_result_dict)
        except Exception as e:
            error_message += "{filename}::{e}\n".format(filename=filename, e = e)
    return rows, error_message

def prepare_complexity_json_data():
    try:
        error_message = ""

        master_json = open('master_data.json', "r").read()
        python_script_dir = os.path.join("network-analytics-pm-explorer", "pm-explorer", "resources", "scripts", "Python")
        complexity_json_data, error_message_tmp = get_the_complexity(python_script_dir, error_message)
        error_message += error_message_tmp
        if error_message == "":
            dumped_data = json.dumps(complexity_json_data)

            complexity_files = {'master_data.json': master_json, 
                                'latest_data.json': dumped_data}
        else:
            complexity_files = {}
        return complexity_files, error_message
    except Exception as e:
        print("44: ", (sys.exc_info()[2]).tb_lineno, e)

def html_table_generate(table_content):
    
    jquery_content = """
$(document).ready(function(){
    $('.dataframe td:nth-child(7)').each(function(){
        if ($(this).text() == "Fail") {
            $(this).parent().css("background-color","#f79a86");
        }
    });
});
"""

    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<title>PMEx: Complexity</title>
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.js"></script>
<script type="text/javascript">

{jquery_content}

</script>

</head>
<body>
<figure>
    <figcaption>PM Explorer Cyclomatic Complexity</figcaption>
    {table_content}

</figure>
</body>
</html>
""".format(jquery_content = jquery_content, table_content = table_content)
    open("result.html", "w").write(html_content)

def compare_json_data(complexity_files):
    
    rank_grade_value = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6}

    latest_repo = complexity_files['latest_data.json']
    master_repo = complexity_files['master_data.json'] 

    latest_repo_dict = json.loads(latest_repo)
    master_repo_dict = json.loads(master_repo)

    rank_grade_status = set()

    report_script_dict = []
    row = []
    all_script_names = set(latest_repo_dict.keys()) | set(master_repo_dict.keys())
    for script_name in all_script_names:
        
        latest_def_names_dict = latest_repo_dict.get(script_name, None)
        master_def_names_dict = master_repo_dict.get(script_name, None)

        if latest_def_names_dict and master_def_names_dict:
            for def_name, value_dict in latest_def_names_dict.items():
                latest_rank_grade = value_dict.get("complexity_rank")
                latest_code_rank = rank_grade_value.get(latest_rank_grade)
                latest_rank_value = value_dict.get("complexity_value")
                if def_name in master_def_names_dict:
                    master_rank_grade = master_def_names_dict[def_name]["complexity_rank"]
                    master_code_rank = rank_grade_value.get(master_rank_grade)
                    master_rank_value = master_def_names_dict[def_name]["complexity_value"]
                    rank_status = "Pass" if (latest_code_rank <= master_code_rank or latest_code_rank < 3) and (latest_rank_value <= master_rank_value or latest_code_rank < 3) else "Fail"
                else:
                    master_rank_grade = None; master_rank_value = None
                    rank_status = "Pass" if latest_code_rank < 3 else "Fail"
                    
                rank_grade_status.add(rank_status)

                #print(def_name, value_dict.get("complexity_rank"), value_dict.get("complexity_value"))

                row.append((script_name, def_name, master_rank_grade, master_rank_value, latest_rank_grade, latest_rank_value, rank_status))
        elif latest_def_names_dict and not master_def_names_dict:
            master_rank_grade = None; master_rank_value = None
            for def_name, value_dict in latest_def_names_dict.items():
                latest_rank_grade   = value_dict.get("complexity_rank")
                latest_code_rank    = rank_grade_value.get(latest_rank_grade)
                latest_rank_value   = value_dict.get("complexity_value")
                rank_status = "Pass" if latest_code_rank < 3 else "Fail"

                row.append((script_name, def_name, master_rank_grade, master_rank_value, latest_rank_grade, latest_rank_value, rank_status))
                rank_grade_status.add(rank_status)
        elif master_def_names_dict and not latest_def_names_dict:
            latest_rank_grade = None; latest_rank_value = None
            for def_name, value_dict in master_def_names_dict.items():
                master_rank_grade   = value_dict.get("complexity_rank")
                master_code_rank    = rank_grade_value.get(master_rank_grade)
                master_rank_value   = value_dict.get("complexity_value")
                rank_status = "Pass"
                
                row.append((script_name, def_name, master_rank_grade, master_rank_value, latest_rank_grade, latest_rank_value, rank_status))
                rank_grade_status.add(rank_status)
        else:
            latest_rank_grade = None; latest_rank_value = None; master_rank_grade = None; master_rank_value = None
            row.append((script_name, None, master_rank_grade, master_rank_value, latest_rank_grade, latest_rank_value, None))
            rank_grade_status.add("Pass")
        
        report_script_dict.append(row)

    df = pandas.DataFrame(row, columns = ["script name", "def name", "master branch cyclomatic rank", "master branch cyclomatic value", "Latest push cyclomatic rank", "Latest push cyclomatic value", "status"])
    sorted_df = df.sort_values(['status', 'Latest push cyclomatic value', 'script name', 'master branch cyclomatic value'], ascending=[True, False, True, False], na_position = 'last')
    result = sorted_df.to_html(index = True, justify = "center", table_id = "cyclomatic_table")
    html_table_generate(result)

    return 1 if "Fail" in rank_grade_status else 0

def generate_error_html(error_message):
    splitted_text = error_message.split("====")
    error_text_format = [text.split("::") for text in (splitted_text[0]).split("\n") if text]
    print("error_text_format", error_text_format)
    
    df = pandas.DataFrame(error_text_format, columns = ["script name", "Error Description"])
    sorted_df = df.sort_values(['script name'], ascending=[True], na_position = 'last')
    result = sorted_df.to_html(index = False, justify = "center", table_id = "cyclomatic_table")
    html_table_generate(result)
    #open("result.html", "w").write(error_message)

def update_master_json(complexity_files):
    master_repo = complexity_files['master_data.json']
    current_dir =  os.path.dirname(os.path.realpath(__file__))
    master_file = os.path.join(current_dir, 'master_data.json')
    open(master_file, "w").write(master_repo)
    print("master updated")

def get_command_line_args():
    """reads users entry for python script
    Returns:
        dict: dictionary of arguments parsed
    """
    parser = argparse.ArgumentParser("Calculate Cyclomatic Complexity")
    parser.add_argument("-b", "--branch_name", help = "Current Branch Name", type = str)
  
    argument_values = parser.parse_args()
  
    return argument_values.branch_name

branch_name = get_command_line_args()
pandas.set_option('display.max_colwidth', -1)

try:
    error_message = ""
    
    complexity_files, error_message = prepare_complexity_json_data()
    if complexity_files != {} and error_message == "":
        complexity_exit_code = compare_json_data(complexity_files)
        if branch_name == "master" and complexity_exit_code == 0:
            update_master_json(complexity_files)
        #print("complexity_exit_code", complexity_exit_code)
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #print(exc_type, fname, exc_tb.tb_lineno)
    complexity_exit_code = 1
    error_message += "\n"+ "====" + "\n" + "-"*88 + "\nexc_type: {exc_type}, filename: {fname}\n{e}: {line_num}".format(exc_type = exc_type, fname = fname, line_num = exc_tb.tb_lineno, e = e)

if error_message:
    generate_error_html(error_message)
    return_exit_code    = 1
else:
    return_exit_code    = complexity_exit_code


#exit code - 0 --> Success
#exit code - 1 --> Failed 
os._exit(return_exit_code)
