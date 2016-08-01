import subprocess
import sys
import json

file_path=sys.argv[1]
soslist = []
tuned_active=["/usr/bin/cat", "%s/sos_commands/tuned/tuned-adm_active_2" % (file_path)]
tuned_recommend=["/usr/bin/cat", "%s/sos_commands/tuned/tuned-adm_recommend_2" % (file_path)]
active_profile=subprocess.check_output(tuned_active).rstrip()
recommend_profile=subprocess.check_output(tuned_recommend).rstrip()
if active_profile == "No current active profile.":
        active_profile = "none"
data = json.dumps({ 'tuned': {
        'active': [
            active_profile
        ],
        'recommend': [
            recommend_profile
        ]
}})
print data
