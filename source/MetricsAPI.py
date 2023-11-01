class MetricsAPI:

    def storeIssueTypes(database):
        """Insert the existing Issue types in database."""
        pass

    def getNumberOfExperimentalBlocks(blocks, numberOfExperimentalBlocks):
        """Get number of blocks of the Experimental category."""
        pass

    def getNumberOfLegoBlocks(blocks, numberOfLegoBlocks):
        """Get number of blocks of the Lego category."""
        pass

    def getNumberOfConnectivityBlocks(blocks, numberOfConnectivityBlocks):
        """Get number of blocks of the Connectivity category."""
        pass

    def getNumberOfStorageBlocks(blocks, numberOfStorageBlocks):
        """Get number of blocks of the Storage category."""
        pass

    def getNumberOfSocialBlocks(blocks, numberOfSocialBlocks):
        """Get number of blocks of the Social category."""
        pass

    def getNumberOfSensorsBlocks(blocks, numberOfSensorsBlocks):
        """Get number of blocks of the Sensors category."""
        pass

    def getNumberOfChartsBlocks(blocks, numberOfChartsBlocks):
        """Get number of blocks of the Charts category."""
        pass

    def getNumberOfMapsBlocks(blocks, numberOfMapsBlocks):
        """Get number of blocks of the Maps category."""
        pass

    def getNumberOfDrawingAnimationBlocks(blocks, numberOfDrawingAnimationBlocks):
        """Get number of blocks of the Drawing and Animation category."""
        pass

    def getNumberOfMediaBlocks(blocks, numberOfMediaBlocks):
        """Get number of blocks of the Media category."""
        pass

    def getNumberOfLayoutBlocks(blocks, numberOfLayoutBlocks):
        """Get number of blocks of the Layout category."""
        pass

    def getNumberOfUserInterfaceBlocks(blocks, numberOfUserInterfaceBlocks):
        """Get number of blocks of the User Interface category."""
        pass

    def getNumberOfNoneCaseDefinedFunctionalBlocks(blocks, numberOfNoneCaseDefinedFunctionalBlocks, projectID, screenName, database):
        """Get number of defined Functional blocks with defined names using None case."""
        pass

    def getNumberOfNoneCaseVariables(blocks, numberOfNoneCaseVariables, projectID, screenName, database):
        """Get number of defined variables blocks with defined names using None case."""
        pass

    def getNumberOfSnakeCaseDefinedFunctionalBlocks(blocks, numberOfSnakeCaseDefinedFunctionalBlocks, projectID, screenName, database):
        """Get number of defined Functional blocks with defined names using Snake case."""
        pass

    def getNumberOfSnakeCaseVariables(blocks, numberOfSnakeCaseVariables, projectID, screenName, database):
        """Get number of defined variables blocks with defined names using Snake case."""
        pass

    def getNumberOfPascalCaseDefinedFunctionalBlocks(blocks, numberOfPascalCaseDefinedFunctionalBlocks, projectID, screenName, database):
        """Get number of defined Functional blocks with defined names using Pascal case."""
        pass

    def getNumberOfPascalCaseVariables(blocks, numberOfPascalCaseVariables, projectID, screenName, database):
        """Get number of defined variables blocks with defined names using Pascal case."""
        pass

    def getNumberOfCamelCaseDefinedFunctionalBlocks(blocks, numberOfCamelCaseDefinedFunctionalBlocks, projectID, screenName, database):
        """Get number of defined Functional blocks with defined names using Camel case."""
        pass

    def getNumberOfCamelCaseVariables(blocks, numberOfCamelCaseVariables, projectID, screenName, database):
        """Get number of defined variables blocks with defined names using Pascal case."""
        pass

    def getNumberOfVariablesInConditionNotUpdated(blocks, numberOfVariablesInConditionNotUpdated, projectID, screenName, database):
        """Get number of not updated variables used in conditions."""
        pass

    def getNumberOfWhileLoopsWithoutCondition(blocks, numberOfWhileLoopsWithoutCondition, projectID, screenName, database):
        """Get number of while loops blocks without defined condition."""
        pass

    def getNumberOfFunctionalBlocksWithoutReturn(blocks, numberOfFunctionalBlocksWithoutReturn, projectID, screenName, database):
        """Get number of defined Functional blocks without return block."""
        pass

    def getNumberOfDefinedFunctionalBlocksNotUsed(blocks, numberOfDefinedFunctionalBlocksNotUsed, projectID, screenName, database):
        """Get number of defined Functional blocks not used."""
        pass

    def getNumberOfDivisionByZero(blocks, numberOfDivisionByZero, projectID, screenName, database):
        """Get number of division blocks with zero denominator used."""
        pass

    def getNumberOfInfiniteLoops(blocks, numberOfInfiniteLoops, projectID, screenName, database):
        """Get number of infinite loops."""
        pass

    def getNumberOfVariablesNotInitialized(blocks, numberOfVariablesNotInitialized, projectID, screenName, database):
        """Get number of variables not initialized."""
        pass

    def getNumberOfIndexOutOfRange(blocks, numberOfIndexOutOfRange, projectID, screenName, database):
        """Get number of vector with index out of range used."""
        pass

    def getNumberOfDefinedFunctionalBlocks(blocks, numberOfDefinedFunctionalBlocks):
        """Get number of defined Functional blocks."""
        pass

    def getNumberOfUsedFunctionalBlocks(blocks, numberOfUsedFunctionalBlocks):
        """Get number of used Functional blocks."""
        pass

    def getNumberOfEventsBlocks(blocks, numberOfEventsBlocks):
        """Get number of defined Events blocks."""
        pass

    def getNumberOfConditionalBlocks(blocks, numberOfConditionalBlocks):
        """Get number of Conditionals blocks."""
        pass

    def getNumberOfLoopsBlocks(blocks, numberOfLoopsBlocks):
        """Get number of Loops blocks."""
        pass

    def getNumberOfGlobalVariables(blocks, numberOfGlobalVariables):
        """Get number of Global variables blocks."""
        pass

    def getNumberOfLocalVariables(blocks, numberOfLocalVariables):
        """Get number of Local variables blocks."""
        pass

    def getNumberOfScreensError(numberOfScreens, projectID, screenName, database):
        """Check if the application has more than 10 Screens (0/1)."""
        pass

    def getNumberOfDuplicateBlocks(blocks, numberOfDuplicateBlocks, numberOfAnalyzedBlocks):
        """Get number of duplicated blocks."""
        pass

    def getVariablesWithNamesTooShorts(blocks, errorsVariablesNames, projectID, screenName, database):
        """Get number of variables with name more shorts than 3 characters."""
        pass

    def getFunctionsWithNamesTooShorts(blocks, errorsFunctionsNames, projectID, screenName, database):
        """Get number of Functional blocks with names more shorts than 3 characters."""
        pass

    def getFunctionsWithTooManyParameters(blocks, errorsNumberOfArguments, projectID, screenName, database):
        """Get number of Functional blocks with too many parameters (more than 3 parameters)."""
        pass

    def getVariablesNotUsed(blocks, errorsValuesNotUsed, projectID, screenName, database):
        """Get number of variables not used."""
        pass

    def getNumberOfComments(comments, numberOfComments):
        """Get number of Comment blocks."""
        pass

    def getMagicNumbers(blocks, magicNumbers, projectID, screenName, database):
        """Get number of used Magic numbers."""
        pass

    def getFunctionsWithTooManyBlocks(blocks, numberOfFunctionsWithTooManyBlocks, projectID, screenName, database):
        """Get number of defined Functional blocks with too many blocks (more than 15 blocks)."""
        pass

    def getIfBlocksTooManyNested(blocks, ifBlocksTooManyNested, projectID, screenName, database):
        """Get number of If blocks too many nested (more than 3 levels)."""
        pass

    def getCiclomaticComplexityPerFunction(blocks):
        """Calculate Ciclomatic Complexity."""
        pass

    def getCognitiveComplexityPerFunction(blocks):
        """Calculate Cognitive Complexity."""
        pass