#!/usr/bin/python

import boto3
import sys
from boto.mturk.connection import MTurkConnection
from boto.mturk.question import HTMLQuestion

MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'

mturk = boto3.client('mturk',
   aws_access_key_id = "AKIAJN57M3LJ25KIDO7A",
   aws_secret_access_key = "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",
   region_name='us-east-1',
   endpoint_url = MTURK_SANDBOX
)

# You will need the following library
# to help parse the XML answers supplied from MTurk
# Install it in your local environment with
# pip install xmltodict
import xmltodict

# Use the hit_id previously created
hit_id = '3126F2F5F72IF38SIOHLBNGASGREPU'

# We are only publishing this task to one Worker
# So we will get back an array with one item if it has been completed

worker_results = mturk.list_assignments_for_hit(HITId=hit_id, AssignmentStatuses=['Submitted'])

#print type(worker_results)
#print worker_results['NumResults']
#print worker_results['Assignments'][0]

#for entry in worker_results['Assignments'][0]:
#    print entry, ':', worker_results['Assignments'][0][entry]

#print worker_results['Assignments'][0]['AutoApprovalTime']

if worker_results['NumResults'] > 0:
   for assignment in worker_results['Assignments']:
      xml_doc = xmltodict.parse(assignment['Answer'])
      
      print "Worker's answer was:"
      if type(xml_doc['QuestionFormAnswers']['Answer']) is list:
         # Multiple fields in HIT layout
         for answer_field in xml_doc['QuestionFormAnswers']['Answer']:
            print "For multiple input fields: " + answer_field['QuestionIdentifier']
            print "Submitted answer: " + answer_field['FreeText']
      else:
         # One field found in HIT layout
         print "For one input field: " + xml_doc['QuestionFormAnswers']['Answer']['QuestionIdentifier']
         print "Submitted answer: " + xml_doc['QuestionFormAnswers']['Answer']['FreeText']
else:
   print "No results ready yet"
