## @file
# Check JSON result from GitHub API to check if submitter of a pull request is
# an active memory of a team with permissions to submit a pull request.
#
# Copyright (c) 2019, Intel Corporation. All rights reserved.<BR>
# SPDX-License-Identifier: BSD-2-Clause-Patent
#
# https://developer.github.com/v3/teams/members/#get-team-membership
#

'''
CheckMembership
'''

import os
import sys
import requests

headers = {
  'Authorization': 'token ' + os.environ['GitHubPAT'],
}

try:
  user = os.environ['SYSTEM_PULLREQUEST_SOURCEREPOSITORYURI'].split('/')[3]
except:
  print ('PR URL is not valid')
  sys.exit (1)

response = requests.get('https://api.github.com/teams/1649488/memberships/' + user, headers=headers)

Membership = response.json()
if 'state' not in Membership:
  print ('PR submitter ' + user + ' not found')
  sys.exit (1)
if 'role' not in Membership:
  print ('PR submitter ' + user + ' not found')
  sys.exit (1)
if Membership['state'] not in ['active']:
  print ('PR submitter ' + user + ' is not active')
  sys.exit (1)
if Membership['role'] not in ['member', 'maintainer']:
  print ('PR submitter ' + user + ' is not a member or maintainer')
  sys.exit (1)
print ('PR submitter ' + user + ' is active ' + Membership['role'])
