# Copyright 2016 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Creates Compute Engine instance and boot disk resources.
"""

import yaml


def GenerateEmbeddableYaml(yaml_string):
    # This function takes a string in YAML format and produces
    # an equivalent YAML representation that can be
    # inserted into another YAML document.
    yaml_object = yaml.load(yaml_string)
    dumped_yaml = yaml.dump(yaml_object, default_flow_style=True)
    return dumped_yaml


def GenerateConfig(context):
    return """
resources:
  - type: compute.v1.instance
    name: %(name)s
    properties:
      tags: 
        items: 
          - http
      zone: %(zone)s
      machineType: https://www.googleapis.com/compute/v1/projects/%(project)s/zones/%(zone)s/machineTypes/%(machine)s
      metadata:
        items:
        - key: sql-ip
          value: %(sql-address)s
        - key: sql-pw
          value: %(password)s
        - key: startup-script-url
          value: %(script)s
      disks:
      - deviceName: boot
        boot: true
        autoDelete: true
        mode: READ_WRITE
        type: PERSISTENT
        initializeParams:
          sourceImage: https://www.googleapis.com/compute/v1/projects/%(project)s/global/images/%(image)s
      networkInterfaces:
        - accessConfigs:
          - name: external-nat
            type: ONE_TO_ONE_NAT
            natIP: %(vm-address)s
          network: https://www.googleapis.com/compute/v1/projects/%(project)s/global/networks/default
      serviceAccounts:
        - email: default
          scopes:
           - https://www.googleapis.com/auth/devstorage.read_only
           - https://www.googleapis.com/auth/logging.write
""" % {"name": context.env["name"],
       "project": context.env["project"],
       "zone": context.properties["zone"],
       "machine": context.properties["machine"],
       "sql-address": context.properties["sql_ip"],
       "password": context.properties["sql_pw"],
       "script": context.properties["startup_script_url"],
       "vm-address": context.properties["nat_IP"],
       "image": context.properties["image"]}

