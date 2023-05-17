# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import openstack

cloud   = "otcdomain"       # your clouds.yaml cloud environment comes here
region  = "eu-de"           # has to match the resources in `cloud`

def userdetails(userid):
    try:
        user = conn.identity.get_user(userid)
    except:
        return "formerly user #" + userid, "UNKNOWN OWNER"
    return user.name, user.email

def main():
    # Create a working connection to OpenStack
    conn = openstack.connect(cloud=cloud)

    projects = [(project.id,
                project.name,
                conn.connect_as_project(project=project.name))
                for project in conn.identity.projects() if region in project.name]

    for pid, pname, pco in projects:
        print(f"Project {pname} ({pid}):")

        # Retrieve all servers in the project
        servers = [(server.id,
                    server.name,
                    server.user_id,
                    server.created_at)
                for server in pco.compute.servers()]
        for id, name, ownerid, created in servers:
            owner, email = userdetails(ownerid)
            print(f"  Server {id} ({name}) {owner}")
            print(f"         created {created} by {email}")

            attachments = [(volume.id, volume.name) for volume in pco.compute.volume_attachments(server=id)]
            for id, name in attachments:
                vtype = pco.volume.find_volume(id).volume_type
                print(f"      Volume {id} ({name}): {vtype}")

if __name__ == '__main__':
    main()
