if __name__ == "__main__":
    cluster_name = 'gocd-prod'
    params = ['dev', 'qa', 'staging']
    if 'prod' in params:
        cluster_name = 'gocd-staging'
    print(cluster_name)
    dict_list = {'key': 'a', 'k2': 'b'}
    print(dict_list.ge)
