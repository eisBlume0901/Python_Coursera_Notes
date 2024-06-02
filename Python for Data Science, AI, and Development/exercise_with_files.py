# Goal: To separate active members to inactive members

def separateMemberStatus(activeMembersFile, inactiveMembersFile):
    with open("members.txt", "r+") as membersFile:
        with open("inactive_members.txt", "a+") as inactiveMembersFile:
            membersFile.seek(0)
            members = membersFile.readlines() # Saves all long string/data/contents in this variable
            header = members[0] # Retrieves the header
            members.pop(0) # Removes the header

            inactive_members = []
            for member in members:
                if "no" in member:
                    inactive_members.append(member)

            inactiveMembersFile.seek(0) # Starts at the first or the 0th index
            inactiveMembersFile.write(header)

            membersFile.seek(0)
            membersFile.write(header)
            for member in members:
                if member in inactive_members:
                    inactiveMembersFile.write(member)
                else:
                    membersFile.write(member)
            membersFile.truncate()

separateMemberStatus("members.txt", "inactive_members.txt")