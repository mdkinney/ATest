## @file
# Use GitHub API to check if submitter of a pull request is an active member of
# a team with permissions to submit a pull request.
#
# Copyright (c) 2019, Intel Corporation. All rights reserved.<BR>
# SPDX-License-Identifier: BSD-2-Clause-Patent
#
# https://developer.github.com/v3/teams/members/#get-team-membership
#
##

'''
CheckGitHubTeamMembership <Token> <Team#> <PR URI>
'''

import sys
import requests

#
# Check number of arguments
#
if len(sys.argv) < 4:
    print('CheckGitHubTeamMembership: Too few arguments.')
    print('  Usage: CheckGitHubTeamMembership <Token> <Team#> <PR URI>')
    sys.exit(1)

#
# Fill in Authorization token using Personal Access Token (PAT)
#
Headers = {
    'Authorization': 'token ' + sys.argv[1],
}

#
# Parse GitHub user ID from PR URI
#
User = sys.argv[3].split('/')
if len(User) < 4:
    print('CheckGitHubTeamMembership: Can not parse PR GitHub ID from PR URI')
    sys.exit(1)
User = User[3]

#
# Generate GitHub API request and parse the JSON response
#
Url = 'https://api.github.com/teams/{Team}/memberships/{User}'.format(
        Team=sys.argv[2],
        User=User
        )
Membership = requests.get(Url, headers=Headers).json()

#
# If JSON response does not contain a 'state' or 'role' field, then exit with
# an error.
#
if 'state' not in Membership or 'role' not in Membership:
    print('CheckGitHubTeamMembership: User {User} not found.'
          .format(User=User))
    sys.exit(1)
#
# If JSON response does not show the user as active, then exit with an error.
#
if Membership['state'] not in ['active']:
    print('CheckGitHubTeamMembership: User {User} is not active.'
          .format(User=User))
    sys.exit(1)
#
# If JSON response does not show the user with a role of member or maintainer,
# then exit with an error
#
if Membership['role'] not in ['member', 'maintainer']:
    print('CheckGitHubTeamMembership: User {User} is not a member/maintainer.'
          .format(User=User))
    sys.exit(1)
#
# JSON response indicates that user is an active member/maintainer.  Exit
# with success.
#
print('CheckGitHubTeamMembership: User {User} is active {Role}.'
      .format(User=User, Role=Membership['role']))
