#!/bin/bash

# create a bucket for the backup
gsutil mb gs://cpo200-sql-migration-$1/

# change the ACL so that the sevice account of the original Cloud SQL instance can write to bucket
gsutil acl ch -u $(gcloud sql instances describe guestbook-sql | grep serviceAccountEmailAddress | awk -F $': ' '{print $2}'):W gs://cpo200-sql-migration-$1/ 

# export the contents of the original guestbook-sql instance
gcloud sql instances export guestbook-sql gs://cpo200-sql-migration-$1/backup.sql

# change the acl on the exported data so that the service account of the new Cloud SQL instance can read it
gsutil acl ch -u $(gcloud sql instances describe guestbook-3-sql | grep serviceAccountEmailAddress | awk -F $': ' '{print $2}'):R gs://cpo200-sql-migration-$1/backup.sql 

# import the data into the new Cloud SQL instance 
gcloud sql instances import guestbook-3-sql gs://cpo200-sql-migration-$1/backup.sql

# set the password on the Cloud SQL instance
gcloud sql instances set-root-password guestbook-3-sql --password $2
