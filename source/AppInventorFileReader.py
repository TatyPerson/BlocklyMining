from FileReaderAPI import FileReaderAPI
from CSVFileWriter import CSVFileWriter
from AppInventorMetrics import AppInventorMetrics
from MySQLDataBase import MySQLDataBase
from xml.dom import minidom
import os
from datetime import datetime
import sys, os
import re
import configparser

class AppInventorFileReader(FileReaderAPI):

	def readFiles(rootdir, database):
		print(f'\n- Printing columns in CSV results file..')
		ProjectID = ['ProjectID']
		ProjectName = ['ProjectName']
		AppName = ['AppName']
		AppVersionCode = ['AppVersionCode']
		AppVersionName = ['AppVersionName']
		NumberOfScreens = ['NumberOfScreens']
		NumberOfTotalBlocks = ['NumberOfTotalBlocks']
		NumberOfDefinedFunctionalBlocks = ['NumberOfDefinedFunctionalBlocks']
		NumberOfUsedFunctionalBlocks = ['NumberOfUsedFunctionalBlocks']
		NumberOfEventsBlocks = ['NumberOfEventsBlocks']
		NumberOfConditionalBlocks = ['NumberOfConditionalBlocks']
		NumberOfLoopsBlocks = ['NumberOfLoopsBlocks']
		NumberOfGlobalVariables = ['NumberOfGlobalVariables']
		NumberOfLocalVariables = ['NumberOfLocalVariables']
		NumberOfUserInterfaceBlocks = ['NumberOfUserInterfaceBlocks']
		NumberOfLayoutBlocks = ['NumberOfLayoutBlocks']
		NumberOfMediaBlocks = ['NumberOfMediaBlocks']
		NumberOfDrawingAnimationBlocks = ['NumberOfDrawingAnimationBlocks']
		NumberOfMapsBlocks = ['NumberOfMapsBlocks']
		NumberOfChartsBlocks = ['NumberOfChartsBlocks']
		NumberOfSensorsBlocks = ['NumberOfSensorsBlocks']
		NumberOfSocialBlocks = ['NumberOfSocialBlocks']
		NumberOfStorageBlocks = ['NumberOfStorageBlocks']
		NumberOfConnectivityBlocks = ['NumberOfConnectivityBlocks']
		NumberOfLegoBlocks = ['NumberOfLegoBlocks']
		NumberOfExperimentalBlocks = ['NumberOfExperimentalBlocks']
		NumberOfScreensErrors = ['NumberOfScreensErrors']
		PercentageDuplicateBlocks = ['PercentageDuplicateBlocks']
		NameOfVariablesErrors = ['NameOfVariablesErrors']
		NameOfFunctionsErrors = ['NameOfFunctionsErrors']
		NumberOfParamatersErrors = ['NumberOfParamatersErrors']
		VariablesNotUsed  = ['VariablesNotUsed']
		PercentageComments = ['PercentageComments']
		MagicNumbers = ['MagicNumbers']
		NumberOfFunctionsWithTooManyBlocks = ['NumberOfFunctionsWithTooManyBlocks']
		NumberOfIfBlocksTooManyNested = ['NumberOfIfBlocksTooManyNested']
		MinCiclomaticComplexity = ['MinCiclomaticComplexity']
		MaxCiclomaticComplexity = ['MaxCiclomaticComplexity']
		AvgCiclomaticComplexity = ['AvgCiclomaticComplexity']
		MinCognitiveComplexity = ['MinCognitiveComplexity']
		MaxCognitiveComplexity = ['MaxCognitiveComplexity']
		AvgCognitiveComplexity = ['AvgCognitiveComplexity']
		NumberOfDivisionByZero = ['NumberOfDivisionByZero']
		NumberOfInfiniteLoops = ['NumberOfInfiniteLoops']
		NumberOfVariablesNotInitialized = ['NumberOfVariablesNotInitialized']
		NumberOfIndexOutOfRange = ['NumberOfIndexOutOfRange']
		NumberOfDefinedFunctionalBlocksNotUsed = ['NumberOfDefinedFunctionalBlocksNotUsed']
		NumberOfFunctionalBlocksWithoutReturn = ['NumberOfFunctionalBlocksWithoutReturn']
		NumberOfWhileLoopsWithoutCondition = ['NumberOfWhileLoopsWithoutCondition']
		NumberOfVariablesInConditionNotUpdated = ['NumberOfVariablesInConditionNotUpdated']
		NumberOfCamelCaseVariales = ['NumberOfCamelCaseVariables']
		NumberOfCamelCaseDefinedFunctionalBlocks = ['NumberOfCamelCaseDefinedFunctionalBlocks']
		NumberOfPascalCaseVariales = ['NumberOfPascalCaseVariables']
		NumberOfPascalCaseDefinedFunctionalBlocks = ['NumberOfPascalCaseDefinedFunctionalBlocks']
		NumberOfSnakeCaseVariables = ['NumberOfSnakeCaseVariables']
		NumberOfSnakeCaseDefinedFunctionalBlocks = ['NumberOfSnakeCaseDefinedFunctionalBlocks']
		NumberOfNoneCaseVariables = ['NumberOfNoneCaseVariables']
		NumberOfNoneCaseDefinedFunctionalBlocks = ['NumberOfNoneCaseDefinedFunctionalBlocks']

		csvNumberFile = 0
		currentDate = datetime.today().strftime('%d%m%Y')
		csvFile = f'BlockyMining_AppInventor_{currentDate}_{csvNumberFile}.csv'

		columns = [p for p in zip(
		  ProjectID,
		  ProjectName,
		  AppName,
		  AppVersionCode,
		  AppVersionName,
		  NumberOfScreens,
		  NumberOfTotalBlocks,
		  NumberOfDefinedFunctionalBlocks,
		  NumberOfUsedFunctionalBlocks,
		  NumberOfEventsBlocks, 
		  NumberOfConditionalBlocks,
		  NumberOfLoopsBlocks,
		  NumberOfGlobalVariables,
		  NumberOfLocalVariables,
		  NumberOfUserInterfaceBlocks,
		  NumberOfLayoutBlocks,
		  NumberOfMediaBlocks,
		  NumberOfDrawingAnimationBlocks,
		  NumberOfMapsBlocks,
		  NumberOfChartsBlocks,
		  NumberOfSensorsBlocks,
		  NumberOfSocialBlocks,
		  NumberOfStorageBlocks,
		  NumberOfConnectivityBlocks,
		  NumberOfLegoBlocks,
		  NumberOfExperimentalBlocks,
		  NumberOfScreensErrors,
		  PercentageDuplicateBlocks, 
		  NameOfVariablesErrors, 
		  NameOfFunctionsErrors,
		  NumberOfParamatersErrors, 
		  VariablesNotUsed,
		  PercentageComments,
		  MagicNumbers,
		  NumberOfFunctionsWithTooManyBlocks,
		  NumberOfIfBlocksTooManyNested,
		  MinCiclomaticComplexity,
		  MaxCiclomaticComplexity,
		  AvgCiclomaticComplexity,
		  MinCognitiveComplexity,
		  MaxCognitiveComplexity,
		  AvgCognitiveComplexity,
		  NumberOfDivisionByZero,
		  NumberOfInfiniteLoops,
		  NumberOfVariablesNotInitialized,
		  NumberOfIndexOutOfRange,
		  NumberOfDefinedFunctionalBlocksNotUsed,
		  NumberOfFunctionalBlocksWithoutReturn,
		  NumberOfWhileLoopsWithoutCondition,
		  NumberOfVariablesInConditionNotUpdated,
		  NumberOfCamelCaseVariales,
		  NumberOfCamelCaseDefinedFunctionalBlocks,
		  NumberOfPascalCaseVariales,
		  NumberOfPascalCaseDefinedFunctionalBlocks,
		  NumberOfSnakeCaseVariables,
		  NumberOfSnakeCaseDefinedFunctionalBlocks,
		  NumberOfNoneCaseVariables,
		  NumberOfNoneCaseDefinedFunctionalBlocks)]

		CSVFileWriter.createFile(csvFile, columns)

		currentLine = 0
		projectID = ""
		projectName = ""
		appName = ""
		appVersionCode = 0
		appVersionName = ""
		numberOfTotalBlocks = 0
		numberOfScreens = 0
		numberOfDefinedFunctionalBlocks = 0
		numberOfUsedFunctionalBlocks = 0
		numberOfEventsBlocks = 0
		numberOfConditionalBlocks = 0
		numberOfLoopsBlocks = 0
		numberOfGlobalVariables = 0
		numberOfLocalVariables = 0
		numberOfUserInterfaceBlocks = 0
		numberOfLayoutBlocks = 0
		numberOfMediaBlocks = 0
		numberOfDrawingAnimationBlocks = 0
		numberOfMapsBlocks = 0
		numberOfChartsBlocks = 0
		numberOfSensorsBlocks = 0
		numberOfSocialBlocks = 0
		numberOfStorageBlocks = 0
		numberOfConnectivityBlocks = 0
		numberOfLegoBlocks = 0
		numberOfExperimentalBlocks = 0
		numberOfScreensErrors = 0
		numberOfDuplicateBlocks = 0
		numberOfAnalyzedBlocks = 0
		percentageDuplicateBlocks = 0
		errorsVariablesNames = []
		errorsFunctionsNames = []
		errorsNumberOfArguments = 0
		errorsValuesNotUsed = 0
		numberOfComments = 0
		percentageComments = 0  
		magicNumbers = 0        
		ifBlocksTooManyNested = []
		minCiclomaticComplexity = 0
		maxCiclomaticComplexity = 0
		avgCiclomaticComplexity = 0
		minCognitiveComplexity = 0
		maxCognitiveComplexity = 0
		avgCognitiveComplexity = 0
		numberOfFunctionsWithTooManyBlocks = 0
		numberOfDivisionByZero = 0
		numberOfInfiniteLoops = 0
		numberOfVariablesNotInitialized = 0
		numberOfIndexOutOfRange = 0
		numberOfDefinedFunctionalBlocksNotUsed = 0
		numberOfFunctionalBlocksWithoutReturn = 0
		numberOfWhileLoopsWithoutCondition = 0
		numberOfVariablesInConditionNotUpdated = 0
		numberOfCamelCaseVariables = 0
		numberOfCamelCaseDefinedFunctionalBlocks = 0
		numberOfPascalCaseVariables = 0
		numberOfPascalCaseDefinedFunctionalBlocks = 0
		numberOfSnakeCaseVariables = 0
		numberOfSnakeCaseDefinedFunctionalBlocks = 0
		numberOfNoneCaseVariables = 0
		numberOfNoneCaseDefinedFunctionalBlocks = 0

		for subdir, dirs, files in os.walk(rootdir):
		  for file in files:
		    subdirNameSplit = subdir.split('/')
		    currentProjectName = subdirNameSplit[len(subdirNameSplit)-1]
		    path = os.path.join(subdir, file)

		    print(f'\n- projectID: {projectID}')
		    print(f'\n- currentProjectName: {currentProjectName}')

		    if projectID != currentProjectName:

		      if projectID != "" and numberOfTotalBlocks > 0:

		        print('Storing in database..')
		        if database == "mysql":
		        	MySQLDataBase.insertProject(projectID, projectName, database)

		        print('Writing in CSV file..')

		        if numberOfAnalyzedBlocks > 0:
		          percentageDuplicateBlocks = round(((numberOfDuplicateBlocks * 100) / numberOfAnalyzedBlocks), 2)
		        else: 
		          percentageDuplicateBlocks = 0

		        percentageComments = round((numberOfComments * 100) / numberOfTotalBlocks, 2)
		        avgCiclomaticComplexity = round(avgCiclomaticComplexity / numberOfScreens, 2)
		        avgCognitiveComplexity = round(avgCognitiveComplexity / numberOfScreens, 2)

		        newRow = [projectID,
		        projectName,
		        appName,
		        appVersionCode,
		        appVersionName,
		        numberOfScreens,
		        numberOfTotalBlocks,
		        numberOfDefinedFunctionalBlocks, 
		        numberOfUsedFunctionalBlocks, 
		        numberOfEventsBlocks,
		        numberOfConditionalBlocks, 
		        numberOfLoopsBlocks,
		        numberOfGlobalVariables,
		        numberOfLocalVariables,
		        numberOfUserInterfaceBlocks,
		        numberOfLayoutBlocks,
		        numberOfMediaBlocks,
		        numberOfDrawingAnimationBlocks,
		        numberOfMapsBlocks,
		        numberOfChartsBlocks,
		        numberOfSensorsBlocks,
		        numberOfSocialBlocks,
		        numberOfStorageBlocks,
		        numberOfConnectivityBlocks,
		        numberOfLegoBlocks,
		        numberOfExperimentalBlocks,
		        numberOfScreensErrors,
		        percentageDuplicateBlocks,
		        len(errorsVariablesNames), 
		        len(errorsFunctionsNames), 
		        errorsNumberOfArguments, 
		        errorsValuesNotUsed, 
		        percentageComments, 
		        magicNumbers, 
		        numberOfFunctionsWithTooManyBlocks,
		        len(ifBlocksTooManyNested), 
		        minCiclomaticComplexity, 
		        maxCiclomaticComplexity, 
		        avgCiclomaticComplexity, 
		        minCognitiveComplexity, 
		        maxCognitiveComplexity, 
		        avgCognitiveComplexity,
		        numberOfDivisionByZero,
		        numberOfInfiniteLoops,
		        numberOfVariablesNotInitialized,
		        numberOfIndexOutOfRange,
		        numberOfDefinedFunctionalBlocksNotUsed,
		        numberOfFunctionalBlocksWithoutReturn,
		        numberOfWhileLoopsWithoutCondition,
		        numberOfVariablesInConditionNotUpdated,
		        numberOfCamelCaseVariables,
		        numberOfCamelCaseDefinedFunctionalBlocks,
		        numberOfPascalCaseVariables,
		        numberOfPascalCaseDefinedFunctionalBlocks,
		        numberOfSnakeCaseVariables,
		        numberOfSnakeCaseDefinedFunctionalBlocks,
		        numberOfNoneCaseVariables,
		        numberOfNoneCaseDefinedFunctionalBlocks]

		        CSVFileWriter.writeLine(csvFile, newRow)

		        currentLine = currentLine + 1
		        if(currentLine > 500000):
		        	currentLine = 0
		        	csvNumberFile = csvNumberFile + 1
		        	csvFile = f'BlockyMining_AppInventor_{currentDate}_{csvNumberFile}.csv'

		        #Resetting all variables to get the global results by project
		        numberOfScreens = 0
		        numberOfTotalBlocks = 0
		        numberOfDefinedFunctionalBlocks = 0
		        numberOfUsedFunctionalBlocks = 0
		        numberOfEventsBlocks = 0
		        numberOfConditionalBlocks = 0
		        numberOfLoopsBlocks = 0
		        numberOfGlobalVariables = 0
		        numberOfLocalVariables = 0
		        numberOfUserInterfaceBlocks = 0
		        numberOfLayoutBlocks = 0
		        numberOfMediaBlocks = 0
		        numberOfDrawingAnimationBlocks = 0
		        numberOfMapsBlocks = 0
		        numberOfChartsBlocks = 0
		        numberOfSensorsBlocks = 0
		        numberOfSocialBlocks = 0
		        numberOfStorageBlocks = 0
		        numberOfConnectivityBlocks = 0
		        numberOfLegoBlocks = 0
		        numberOfExperimentalBlocks = 0
		        numberOfScreensErrors = 0
		        numberOfAnalyzedBlocks = 0
		        numberOfDuplicateBlocks = 0
		        percentageDuplicateBlocks = 0
		        errorsVariablesNames = []
		        errorsFunctionsNames = []
		        errorsNumberOfArguments = 0
		        errorsValuesNotUsed = 0
		        numberOfComments = 0
		        percentageComments = 0  
		        magicNumbers = 0        
		        ifBlocksTooManyNested = []
		        minCiclomaticComplexity = 0
		        maxCiclomaticComplexity = 0
		        avgCiclomaticComplexity = 0
		        minCognitiveComplexity = 0
		        maxCognitiveComplexity = 0
		        avgCognitiveComplexity = 0
		        numberOfFunctionsWithTooManyBlocks = 0
		        numberOfDivisionByZero = 0
		        numberOfInfiniteLoops = 0
		        numberOfVariablesNotInitialized = 0
		        numberOfIndexOutOfRange = 0
		        numberOfDefinedFunctionalBlocksNotUsed = 0
		        numberOfFunctionalBlocksWithoutReturn = 0
		        numberOfWhileLoopsWithoutCondition = 0
		        numberOfVariablesInConditionNotUpdated = 0
		        numberOfCamelCaseVariables = 0
		        numberOfCamelCaseDefinedFunctionalBlocks = 0
		        numberOfPascalCaseVariables = 0
		        numberOfPascalCaseDefinedFunctionalBlocks = 0
		        numberOfSnakeCaseVariables = 0
		        numberOfSnakeCaseDefinedFunctionalBlocks = 0
		        numberOfNoneCaseVariables = 0
		        numberOfNoneCaseDefinedFunctionalBlocks = 0

		      projectID = currentProjectName

		    if "project.properties" in path:
		      fileName = file
		      print(f'\n- FileName: {fileName}')

		      with open(path, 'r') as f:
		        config_string = '[appinventor_properties]\n' + f.read()
		        config = configparser.RawConfigParser()
		        config.read_string(config_string)
		        if config.has_option('appinventor_properties','name'):
		          projectName = config.get('appinventor_properties','name')
		        else:
		          projectName = ""

		        if config.has_option('appinventor_properties','aname'):
		          appName = config.get('appinventor_properties','aname')
		          appName = re.sub(' ', '_', appName)
		        else:
		          appName = ""

		        if config.has_option('appinventor_properties','versioncode'):  
		          appVersionCode = config.get('appinventor_properties','versioncode')
		        else:
		          appVersionCode = ""

		        if config.has_option('appinventor_properties','versionname'):
		          appVersionName = config.get('appinventor_properties','versionname')
		          appVersionName = re.sub('\\.', '_', appVersionName)
		        else:
		          appVersionName = ""

		    if ".bky" in path:
		      try:
		        fileName = file
		        print(f'\n- FileName: {fileName}')

		        file = minidom.parse(path)

		        blocks = file.getElementsByTagName('block')

		        if len(blocks) > 70: #se descartan los proyectos con poca complejidad

		          screenName = re.sub('.bky', '', fileName)

		          if database == "mysql":
		          	MySQLDataBase.insertScreen(projectID, screenName, len(blocks), database)

		          numberOfScreens = numberOfScreens + 1
		          numberOfTotalBlocks = numberOfTotalBlocks + len(blocks)

		          #--- MÉTRICA ABSOLUTA 1a: NÚMERO DE BLOQUES FUNCIONALES DEFINIDOS

		          numberOfDefinedFunctionalBlocks = AppInventorMetrics.getNumberOfDefinedFunctionalBlocks(blocks, numberOfDefinedFunctionalBlocks)

		          #--- MÉTRICA ABSOLUTA 1b: NÚMERO DE BLOQUES FUNCIONALES USADOS

		          numberOfUsedFunctionalBlocks = AppInventorMetrics.getNumberOfUsedFunctionalBlocks(blocks, numberOfUsedFunctionalBlocks)

		          #--- MÉTRICA ABSOLUTA 2: NÚMERO DE EVENTOS

		          numberOfEventsBlocks = AppInventorMetrics.getNumberOfEventsBlocks(blocks, numberOfEventsBlocks)

		          #--- MÉTRICA ABSOLUTA 3: NÚMERO DE CONDICIONES

		          numberOfConditionalBlocks = AppInventorMetrics.getNumberOfConditionalBlocks(blocks, numberOfConditionalBlocks)

		          #--- MÉTRICA ABSOLUTA 4: NÚMERO DE BUCLES

		          numberOfLoopsBlocks = AppInventorMetrics.getNumberOfLoopsBlocks(blocks, numberOfLoopsBlocks)

		          #--- MÉTRICA ABSOLUTA 5: NÚMERO DE VARIABLES GLOBALES

		          numberOfGlobalVariables = AppInventorMetrics.getNumberOfGlobalVariables(blocks, numberOfGlobalVariables)

		          #--- MÉTRICA ABSOLUTA 6: NÚMERO DE VARIABLES LOCALES

		          numberOfLocalVariables = AppInventorMetrics.getNumberOfLocalVariables(blocks, numberOfLocalVariables)

		          #--- MÉTRICA ABSOLUTA 7: NÚMERO DE BLOQUES DE LA CATEGORIA USER INTERFACE

		          numberOfUserInterfaceBlocks = AppInventorMetrics.getNumberOfUserInterfaceBlocks(blocks, numberOfUserInterfaceBlocks)

		          #--- MÉTRICA ABSOLUTA 8: NÚMERO DE BLOQUES DE LA CATEGORIA LAYOUT

		          numberOfLayoutBlocks = AppInventorMetrics.getNumberOfLayoutBlocks(blocks, numberOfLayoutBlocks)

		          #--- MÉTRICA ABSOLUTA 9: NÚMERO DE BLOQUES DE LA CATEGORIA MEDIA

		          numberOfMediaBlocks = AppInventorMetrics.getNumberOfMediaBlocks(blocks, numberOfMediaBlocks)

		          #--- MÉTRICA ABSOLUTA 10: NÚMERO DE BLOQUES DE LA CATEGORIA DRAWING AND ANIMATION

		          numberOfDrawingAnimationBlocks = AppInventorMetrics.getNumberOfDrawingAnimationBlocks(blocks, numberOfDrawingAnimationBlocks)

		          #--- MÉTRICA ABSOLUTA 11: NÚMERO DE BLOQUES DE LA CATEGORÍA MAPS

		          numberOfMapsBlocks = AppInventorMetrics.getNumberOfMapsBlocks(blocks, numberOfMapsBlocks)

		          #--- MÉTRICA ABSOLUTA 12: NÚMERO DE BLOQUES DE LA CATEGORÍA CHARTS

		          numberOfChartsBlocks = AppInventorMetrics.getNumberOfChartsBlocks(blocks, numberOfChartsBlocks)

		          #--- MÉTRICA ABSOLUTA 13: NÚMERO DE BLOQUES DE LA CATEGORIA SENSORS

		          numberOfSensorsBlocks = AppInventorMetrics.getNumberOfSensorsBlocks(blocks, numberOfSensorsBlocks)

		          #--- MÉTRICA ABSOLUTA 14: NÚMERO DE BLOQUES DE LA CATEGORIA SOCIAL

		          numberOfSocialBlocks = AppInventorMetrics.getNumberOfSocialBlocks(blocks, numberOfSocialBlocks)

		          #--- MÉTRICA ABSOLUTA 15: NÚMERO DE BLOQUES DE LA CATEGORIA STORAGE

		          numberOfStorageBlocks = AppInventorMetrics.getNumberOfStorageBlocks(blocks, numberOfStorageBlocks)

		          #--- MÉTRICA ABSOLUTA 16: NÚMERO DE BLOQUES DE LA CATEGORIA CONNECTIVITY

		          numberOfConnectivityBlocks = AppInventorMetrics.getNumberOfConnectivityBlocks(blocks, numberOfConnectivityBlocks)

		          #--- MÉTRICA ABSOLUTA 17: NÚMERO DE BLOQUES DE LA CATEGORIA LEGO MINDSTORMS

		          numberOfLegoBlocks = AppInventorMetrics.getNumberOfLegoBlocks(blocks, numberOfLegoBlocks)

		          #--- MÉTRICA ABSOLUTA 18: NÚMERO DE BLOQUES DE LA CATEGORIA EXPERIMENTAL

		          numberOfExperimentalBlocks = AppInventorMetrics.getNumberOfExperimentalBlocks(blocks, numberOfExperimentalBlocks)

		            #--- CODE SMELL 1: NÚMERO DE PANTALLAS DEMASIADO ALTO (>10) ---
		          numberOfScreensErrors = AppInventorMetrics.getNumberOfScreensError(numberOfScreens, projectID, screenName, database)

		          #--- CODE SMELL 2: PORCENTAJE DE BLOQUES DUPLICADOS ---

		          numberOfDuplicateBlocks, numberOfAnalyzedBlocks = AppInventorMetrics.getNumberOfDuplicateBlocks(blocks, numberOfDuplicateBlocks, numberOfAnalyzedBlocks)

		          #--- CODE SMELL 3: NOMBRE DE VARIABLES DEMASIADO CORTOS (<3) ---

		          errorsVariablesNames = AppInventorMetrics.getVariablesWithNamesTooShorts(blocks, errorsVariablesNames, projectID, screenName, database)

		          #--- CODE SMELL 4: NOMBRE DE FUNCIONES DEMASIADO CORTOS (<3) ---

		          errorsFunctionsNames = AppInventorMetrics.getFunctionsWithNamesTooShorts(blocks, errorsFunctionsNames, projectID, screenName, database)

		          #--- CODE SMELL 5: FUNCIONES CON DEMASIADOS PARÁMETROS (>3) ---

		          errorsNumberOfArguments = AppInventorMetrics.getFunctionsWithTooManyParameters(blocks, errorsNumberOfArguments, projectID, screenName, database)

		          #--- CODE SMELL 6: VARIABLES DECLARADAS Y NO USADAS ---

		          errorsValuesNotUsed = AppInventorMetrics.getVariablesNotUsed(blocks, errorsValuesNotUsed, projectID, screenName, database)

		          #--- CODE SMELL 7: PORCENTAJE DE USO DE COMENTARIOS ---

		          comments = file.getElementsByTagName('comment')
		          numberOfComments = AppInventorMetrics.getNumberOfComments(comments, numberOfComments)

		          #--- CODE SMELL 8: NÚMERO DE MAGIC NUMBERS ---

		          magicNumbers = AppInventorMetrics.getMagicNumbers(blocks, magicNumbers, projectID, screenName, database)

		          #--- CODE SMELL 9: FUNCIONES CON DEMASIADAS LÍNEAS ---

		          numberOfFunctionsWithTooManyBlocks = AppInventorMetrics.getFunctionsWithTooManyBlocks(blocks, numberOfFunctionsWithTooManyBlocks, projectID, screenName, database)

		          #--- CODE SMELL 10: BLOQUES IF DEMASIADO ANIDADOS (>= 2 NIVELES) ---

		          ifBlocksTooManyNested = AppInventorMetrics.getIfBlocksTooManyNested(blocks, ifBlocksTooManyNested, projectID, screenName, database)

		          #--- MÉTRICA ERRORES COMUNES 1: DIVISIÓN POR CERO ---

		          numberOfDivisionByZero = AppInventorMetrics.getNumberOfDivisionByZero(blocks, numberOfDivisionByZero, projectID, screenName, database)

		          #--- MÉTRICA ERRORES COMUNES 2: BUCLES INFINITOS ---

		          numberOfInfiniteLoops = AppInventorMetrics.getNumberOfInfiniteLoops(blocks, numberOfInfiniteLoops, projectID, screenName, database)

		          #--- MÉTRICA ERRORES COMUNES 3: VARIABLES NO INICIALIZADAS ---

		          numberOfVariablesNotInitialized = AppInventorMetrics.getNumberOfVariablesNotInitialized(blocks, numberOfVariablesNotInitialized, projectID, screenName, database)

		          #--- MÉTRICA ERRORES COMUNES 4: ACCESO A VECTOR CON ÍNDICE FUERA DE RANGO ---

		          numberOfIndexOutOfRange = AppInventorMetrics.getNumberOfIndexOutOfRange(blocks, numberOfIndexOutOfRange, projectID, screenName, database)

		          #--- MÉTRICA ERRORES COMUNES 5: DEFINICIÓN DE PROCEDIMIENTOS/FUNCIONES SIN USAR ---

		          numberOfDefinedFunctionalBlocksNotUsed = AppInventorMetrics.getNumberOfDefinedFunctionalBlocksNotUsed(blocks, numberOfDefinedFunctionalBlocksNotUsed, projectID, screenName, database)

		          #--- MÉTRICA ERRORES COMUNES 6: DEFINICIÓN DE FUNCIONES SIN RETURN ---

		          numberOfFunctionalBlocksWithoutReturn = AppInventorMetrics.getNumberOfFunctionalBlocksWithoutReturn(blocks, numberOfFunctionalBlocksWithoutReturn, projectID, screenName, database)

		          #--- MÉTRICA ERRORES COMUNES 7: DEFINICIÓN DE BUCLE WHILE SIN CONDICIÓN ---

		          numberOfWhileLoopsWithoutCondition = AppInventorMetrics.getNumberOfWhileLoopsWithoutCondition(blocks, numberOfWhileLoopsWithoutCondition, projectID, screenName, database)

		          #--- MÉTRICA ERRORES COMUNES 8: VARIABLES USADAS EN CONDICIÓN SIN ACTUALIZAR ---

		          numberOfVariablesInConditionNotUpdated = AppInventorMetrics.getNumberOfVariablesInConditionNotUpdated(blocks, numberOfVariablesInConditionNotUpdated, projectID, screenName, database)

		          #--- MÉTRICA NOMBRES 1: VARIABLES DEFINIDAS CON CAMEL CASE ---

		          numberOfCamelCaseVariables = AppInventorMetrics.getNumberOfCamelCaseVariables(blocks, numberOfCamelCaseVariables, projectID, screenName, database)

		          #--- MÉTRICA NOMBRES 2: BLOQUES FUNCIONALES DEFINIDOS CON CAMEL CASE ---

		          numberOfCamelCaseDefinedFunctionalBlocks = AppInventorMetrics.getNumberOfCamelCaseDefinedFunctionalBlocks(blocks, numberOfCamelCaseDefinedFunctionalBlocks, projectID, screenName, database)

		          #--- MÉTRICA NOMBRES 3: VARIABLES DEFINIDAS CON PASCAL CASE ---

		          numberOfPascalCaseVariables = AppInventorMetrics.getNumberOfPascalCaseVariables(blocks, numberOfPascalCaseVariables, projectID, screenName, database)

		          #--- MÉTRICA NOMBRES 4: BLOQUES FUNCIONALES DEFINIDOS CON PASCAL CASE ---

		          numberOfPascalCaseDefinedFunctionalBlocks = AppInventorMetrics.getNumberOfPascalCaseDefinedFunctionalBlocks(blocks, numberOfPascalCaseDefinedFunctionalBlocks, projectID, screenName, database)

		          #--- MÉTRICA NOMBRES 5: VARIABLES DEFINIDAS CON SNAKE CASE ---

		          numberOfSnakeCaseVariables = AppInventorMetrics.getNumberOfSnakeCaseVariables(blocks, numberOfSnakeCaseVariables, projectID, screenName, database)

		          #--- MÉTRICA NOMBRES 6: BLOQUES FUNCIONALES DEFINIDOS CON SNAKE CASE ---

		          numberOfSnakeCaseDefinedFunctionalBlocks = AppInventorMetrics.getNumberOfSnakeCaseDefinedFunctionalBlocks(blocks, numberOfSnakeCaseDefinedFunctionalBlocks, projectID, screenName, database)

		          #--- MÉTRICA NOMBRES 7: VARIABLES DEFINIDAS CON NINGÚN FORMATO ---

		          numberOfNoneCaseVariables = AppInventorMetrics.getNumberOfNoneCaseVariables(blocks, numberOfNoneCaseVariables, projectID, screenName, database)

		          #--- MÉTRICA NOMBRES 8: BLOQUES FUNCIONALES DEFINIDOS CON NINGÚN FORMATO ---

		          numberOfNoneCaseDefinedFunctionalBlocks = AppInventorMetrics.getNumberOfNoneCaseDefinedFunctionalBlocks(blocks, numberOfNoneCaseDefinedFunctionalBlocks, projectID, screenName, database)

		          #--- MÉTRICA ANALÍTICA 1: COMPLEJIDAD CICLOMÁTICA ---

		          ciclomaticComplexityPerFunction = AppInventorMetrics.getCiclomaticComplexityPerFunction(blocks)

		          if len(ciclomaticComplexityPerFunction) > 0:
		            if minCiclomaticComplexity == 0:
		              minCiclomaticComplexity = min(ciclomaticComplexityPerFunction)
		            else:
		              currentMinCiclomaticComplexity = min(ciclomaticComplexityPerFunction)
		              minCiclomaticComplexity = min([minCiclomaticComplexity, currentMinCiclomaticComplexity])

		            if maxCiclomaticComplexity == 0:
		              maxCiclomaticComplexity = max(ciclomaticComplexityPerFunction)
		            else:
		              currentMaxCiclomaticComplexity = max(ciclomaticComplexityPerFunction)
		              maxCiclomaticComplexity = max([maxCiclomaticComplexity, currentMaxCiclomaticComplexity])

		            if avgCiclomaticComplexity == 0:
		              avgCiclomaticComplexity = round(sum(ciclomaticComplexityPerFunction) / len(ciclomaticComplexityPerFunction),3)
		            else:
		              currentAvgCiclomaticComplexity = round(sum(ciclomaticComplexityPerFunction) / len(ciclomaticComplexityPerFunction),3)
		              avgCiclomaticComplexity = round(avgCiclomaticComplexity + currentAvgCiclomaticComplexity, 3)

		          #--- MÉTRICA ANALÍTICA 2: COMPLEJIDAD COGNITIVA ---

		          cognitiveComplexityPerFunction = AppInventorMetrics.getCognitiveComplexityPerFunction(blocks)

		          if len(cognitiveComplexityPerFunction) > 0:
		            if minCognitiveComplexity == 0:
		              minCognitiveComplexity = min(cognitiveComplexityPerFunction)
		            else:
		              currentMinCognitiveComplexity = min(cognitiveComplexityPerFunction)
		              minCognitiveComplexity = min([minCognitiveComplexity, currentMinCognitiveComplexity])

		            if maxCognitiveComplexity == 0:
		              maxCognitiveComplexity = max(cognitiveComplexityPerFunction)
		            else:
		              currentMaxCognitiveComplexity = max(cognitiveComplexityPerFunction)
		              maxCognitiveComplexity = max([maxCognitiveComplexity, currentMaxCognitiveComplexity])

		            if avgCognitiveComplexity == 0:
		              avgCognitiveComplexity = round(sum(cognitiveComplexityPerFunction) / len(cognitiveComplexityPerFunction),3)
		            else:
		              currentAvgCognitiveComplexity = round(sum(cognitiveComplexityPerFunction) / len(cognitiveComplexityPerFunction),3)
		              avgCognitiveComplexity = round(avgCognitiveComplexity + currentAvgCognitiveComplexity, 3)

		      except Exception as e:
		        print("Empty bky file..")
		        exc_type, exc_obj, exc_tb = sys.exc_info()
		        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		        print(exc_type, fname, exc_tb.tb_lineno)
		        print(e)


		if projectID != "":
		  print('Writing last project in CSV file..')

		  if numberOfTotalBlocks > 0:
		    if numberOfAnalyzedBlocks > 0:
		      percentageDuplicateBlocks = round(((numberOfDuplicateBlocks * 100) / numberOfAnalyzedBlocks), 2)
		    else: 
		      percentageDuplicateBlocks = 0

		    percentageComments = round((numberOfComments * 100) / numberOfTotalBlocks, 2)
		    avgCiclomaticComplexity = round(avgCiclomaticComplexity / numberOfScreens, 2)
		    avgCognitiveComplexity = round(avgCognitiveComplexity / numberOfScreens, 2)

		    newRow = [projectID,
		    projectName,
		    appName,
		    appVersionCode,
		    appVersionName,
		    numberOfScreens,
		    numberOfTotalBlocks,
		    numberOfDefinedFunctionalBlocks,
		    numberOfUsedFunctionalBlocks,
		    numberOfEventsBlocks,
		    numberOfConditionalBlocks, 
		    numberOfLoopsBlocks,
		    numberOfGlobalVariables,
		    numberOfLocalVariables,
		    numberOfUserInterfaceBlocks,
		    numberOfLayoutBlocks,
		    numberOfMediaBlocks,
		    numberOfDrawingAnimationBlocks,
		    numberOfMapsBlocks,
		    numberOfChartsBlocks,
		    numberOfSensorsBlocks,
		    numberOfSocialBlocks,
		    numberOfStorageBlocks,
		    numberOfConnectivityBlocks,
		    numberOfLegoBlocks,
		    numberOfExperimentalBlocks,
		    numberOfScreensErrors,
		    percentageDuplicateBlocks, 
		    len(errorsVariablesNames), 
		    len(errorsFunctionsNames), 
		    errorsNumberOfArguments, 
		    errorsValuesNotUsed, 
		    percentageComments, 
		    magicNumbers, 
		    numberOfFunctionsWithTooManyBlocks,
		    len(ifBlocksTooManyNested), 
		    minCiclomaticComplexity, 
		    maxCiclomaticComplexity, 
		    avgCiclomaticComplexity, 
		    minCognitiveComplexity, 
		    maxCognitiveComplexity, 
		    avgCognitiveComplexity,
		    numberOfDivisionByZero,
		    numberOfInfiniteLoops,
		    numberOfVariablesNotInitialized,
		    numberOfIndexOutOfRange,
		    numberOfDefinedFunctionalBlocksNotUsed,
		    numberOfFunctionalBlocksWithoutReturn,
		    numberOfWhileLoopsWithoutCondition,
		    numberOfVariablesInConditionNotUpdated,
		    numberOfCamelCaseVariables,
		    numberOfCamelCaseDefinedFunctionalBlocks,
		    numberOfPascalCaseVariables,
		    numberOfPascalCaseDefinedFunctionalBlocks,
		    numberOfSnakeCaseVariables,
		    numberOfSnakeCaseDefinedFunctionalBlocks,
		    numberOfNoneCaseVariables,
		    numberOfNoneCaseDefinedFunctionalBlocks]

		    print('Storing last project in database..')
		    if database == "mysql":
		    	MySQLDataBase.insertProject(projectID, projectName, database)

		    CSVFileWriter.writeLine(csvFile, newRow)

		    currentLine = currentLine + 1
		    if(currentLine > 500000):
		        currentLine = 0
		        csvNumberFile = csvNumberFile + 1
		        csvFile = f'BlockyMining_AppInventor_{currentDate}_{csvNumberFile}.csv'
