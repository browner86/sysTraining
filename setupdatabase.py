from app import db, Topic
db.create_all()



# for i in topic_list:
t_index = Topic("index")
t_task = Topic("text")
t_linux = Topic("linux")
t_windows = Topic("windows")
t_netapp = Topic ("netapp")
t_centrify = Topic ("centrify")
t_security = Topic ("security")
t_network = Topic ("network")
t_hpc = Topic ("hpc")
t_esxi = Topic ("esxi")
t_program = Topic ("program")
t_backups = Topic ("backups")
t_applications = Topic ("applications")
t_inventory = Topic ("inventory")
t_licences = Topic ("licences")
t_administration = Topic ("administration")
t_notes = Topic ("notes")
t_tips = Topic ("tips")

topic_list = [t_index
            , t_task
            , t_linux
            , t_windows
            , t_netapp
            , t_centrify
            , t_security
            , t_network
            , t_hpc
            , t_esxi
            , t_program
            , t_backups
            , t_applications
            , t_inventory
            , t_licences
            , t_administration
            , t_notes
            , t_tips]

db.session.add_all(topic_list)
db.session.commit()