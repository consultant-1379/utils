import os
from jenkis_data import JenkinsData

if __name__ == '__main__':
    '''
    This is the main method code starts from here
    '''
    # Object for class JenkinsData is created
    functional_user_username = os.environ.get('FUNCTIONAL_USER_USERNAME', None)
    functional_user_password = os.environ.get('FUNCTIONAL_USER_PASSWORD', None)
    Jenkins = JenkinsData(functional_user_username, functional_user_password)
    fem_list=[]
    fem_list.append("https://fem5s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins")
    fem_list.append("https://fem6s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins")
    fem_list.append("https://fem7s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins")
    for fem_name in fem_list:
        # Read job names from fem and adding into the job_names file
        job_names=Jenkins.job_names(fem_name)
        # Getting each job build details and calling main functions
        Jenkins.job_time(job_names,fem_name)
