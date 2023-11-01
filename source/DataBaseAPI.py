class DataBaseAPI:

  def openConnection():
    """Open connection with the database."""
    pass

  def insertProject(projectID, projectName, database):
    """Insert Project in the database."""
    pass

  def insertScreen(projectID, screenName, blocksNumber, database):
    """Insert Screen in the database."""
    pass

  def insertIssue(projectID, screenName, blockID, blockType, issueType, database):
    """Insert Issue in the database."""
    pass

  def insertIssueType(issueTypes, database):
    """Insert the Issue types in the database."""
    pass