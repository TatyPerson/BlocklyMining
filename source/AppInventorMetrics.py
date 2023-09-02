import re
from xml.dom.minidom import parseString
from MySQLDataBase import MySQLDataBase
from MetricsAPI import MetricsAPI

userInterfaceComponents = ['Button', 'CheckBox', 'DatePicker', 'Image', 'Label', 'ListPicker', 'ListView', 'Notifier', 'PasswordTextBox', 'Slider', 'Spinner', 'Switch', 'TextBox', 'TimePicker', 'WebViewer']
layoutComponents = ['HorizontalArrangement', 'HorizontalScrollArrangement', 'TableArrangement', 'VerticalArrangement', 'VerticalScrollArrangement']
mediaComponents = ['Camcorder', 'Camera', 'ImagePicker', 'Player', 'Sound', 'SoundRecorder', 'SpeechRecognizer', 'TextToSpeech', 'Translator', 'VideoPlayer']
drawingAnimationComponents = ['Ball', 'Canvas', 'ImageSprite']
mapsComponents = ['Circle', 'FeatureCollection', 'LineString', 'Map', 'Marker', 'Navigation', 'Polygon', 'Rectangle']
chartsComponents = ['Chart', 'ChartData2D']
sensorsComponents = ['AccelerometerSensor', 'BarcodeScanner', 'Barometer', 'Clock', 'GyroscopeSensor', 'Hygrometer', 'LightSensor', 'LocationSensor', 'MagneticFieldSensor', 'NearField', 'OrientationSensor', 'Pedometer', 'ProximitySensor', 'Thermometer']
socialComponents = ['ContactPicker', 'EmailPicker', 'PhoneCall', 'PhoneNumberPicker', 'Sharing', 'Texting', 'Twitter']
storageComponents = ['CloudDB', 'DataFile', 'File', 'Spreadsheet', 'TinyDB', 'TinyWebDB']
connectivityComponents = ['ActivityStarter', 'BluetoothClient', 'BluetoothServer', 'Serial', 'Web']
legoComponents = ['NxtDrive', 'NxtColorSensor', 'NxtLightSensor', 'NxtSoundSensor', 'NxtTouchSensor', 'NxtUltrasonicSensor', 'NxtDirectCommands', 'Ev3Motors', 'Ev3ColorSensor', 'Ev3GyroSensor', 'Ev3TouchSensor', 'Ev3UltrasonicSensor', 'Ev3Sound', 'Ev3UI', 'Ev3Commands']
experimentalComponents = ['FirebaseDB']

snakeRegularExp = r"^[a-zA-Z0-9]+(?:_[a-zA-Z0-9]+)+$"
pascalRegularExp = r"^[A-Z][a-z0-9]+([A-Z][a-z0-9]+)+$"
camelCaseRegularExp = r"^[a-z]+([A-Z][a-z0-9]+)+$"

class AppInventorMetrics(MetricsAPI):

    def getNumberOfExperimentalBlocks(blocks, numberOfExperimentalBlocks):
        for elem in blocks:
            if elem.attributes['type'].value == 'component_method':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in experimentalComponents:
                            numberOfExperimentalBlocks = numberOfExperimentalBlocks + 1
            elif elem.attributes['type'].value == 'component_set_get':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in experimentalComponents:
                            numberOfExperimentalBlocks = numberOfExperimentalBlocks + 1
            elif elem.attributes['type'].value == 'component_event':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in experimentalComponents:
                            numberOfExperimentalBlocks = numberOfExperimentalBlocks + 1
        return numberOfExperimentalBlocks


    def getNumberOfLegoBlocks(blocks, numberOfLegoBlocks):
        for elem in blocks:
            if elem.attributes['type'].value == 'component_method':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in legoComponents:
                            numberOfLegoBlocks = numberOfLegoBlocks + 1
            elif elem.attributes['type'].value == 'component_set_get':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in legoComponents:
                            numberOfLegoBlocks = numberOfLegoBlocks + 1
            elif elem.attributes['type'].value == 'component_event':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in legoComponents:
                            numberOfLegoBlocks = numberOfLegoBlocks + 1
        return numberOfLegoBlocks


    def getNumberOfConnectivityBlocks(blocks, numberOfConnectivityBlocks):
        for elem in blocks:
            if elem.attributes['type'].value == 'component_method':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in connectivityComponents:
                            numberOfConnectivityBlocks = numberOfConnectivityBlocks + 1
            elif elem.attributes['type'].value == 'component_set_get':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in connectivityComponents:
                            numberOfConnectivityBlocks = numberOfConnectivityBlocks + 1
            elif elem.attributes['type'].value == 'component_event':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in connectivityComponents:
                            numberOfConnectivityBlocks = numberOfConnectivityBlocks + 1
        return numberOfConnectivityBlocks


    def getNumberOfStorageBlocks(blocks, numberOfStorageBlocks):
        for elem in blocks:
            if elem.attributes['type'].value == 'component_method':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in storageComponents:
                            numberOfStorageBlocks = numberOfStorageBlocks + 1
            elif elem.attributes['type'].value == 'component_set_get':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in storageComponents:
                            numberOfStorageBlocks = numberOfStorageBlocks + 1
            elif elem.attributes['type'].value == 'component_event':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in storageComponents:
                            numberOfStorageBlocks = numberOfStorageBlocks + 1
        return numberOfStorageBlocks


    def getNumberOfSocialBlocks(blocks, numberOfSocialBlocks):
        for elem in blocks:
            if elem.attributes['type'].value == 'component_method':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in socialComponents:
                            numberOfSocialBlocks = numberOfSocialBlocks + 1
            elif elem.attributes['type'].value == 'component_set_get':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in socialComponents:
                            numberOfSocialBlocks = numberOfSocialBlocks + 1
            elif elem.attributes['type'].value == 'component_event':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in socialComponents:
                            numberOfSocialBlocks = numberOfSocialBlocks + 1
        return numberOfSocialBlocks


    def getNumberOfSensorsBlocks(blocks, numberOfSensorsBlocks):
        for elem in blocks:
            if elem.attributes['type'].value == 'component_method':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in sensorsComponents:
                            numberOfSensorsBlocks = numberOfSensorsBlocks + 1
            elif elem.attributes['type'].value == 'component_set_get':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in sensorsComponents:
                            numberOfSensorsBlocks = numberOfSensorsBlocks + 1
            elif elem.attributes['type'].value == 'component_event':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in sensorsComponents:
                            numberOfSensorsBlocks = numberOfSensorsBlocks + 1
        return numberOfSensorsBlocks


    def getNumberOfChartsBlocks(blocks, numberOfChartsBlocks):
        for elem in blocks:
            if elem.attributes['type'].value == 'component_method':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in chartsComponents:
                            numberOfChartsBlocks = numberOfChartsBlocks + 1
            elif elem.attributes['type'].value == 'component_set_get':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in chartsComponents:
                            numberOfChartsBlocks = numberOfChartsBlocks + 1
            elif elem.attributes['type'].value == 'component_event':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in chartsComponents:
                            numberOfChartsBlocks = numberOfChartsBlocks + 1
        return numberOfChartsBlocks


    def getNumberOfMapsBlocks(blocks, numberOfMapsBlocks):
        for elem in blocks:
            if elem.attributes['type'].value == 'component_method':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in mapsComponents:
                            numberOfMapsBlocks = numberOfMapsBlocks + 1
            elif elem.attributes['type'].value == 'component_set_get':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in mapsComponents:
                            numberOfMapsBlocks = numberOfMapsBlocks + 1
            elif elem.attributes['type'].value == 'component_event':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in mapsComponents:
                            numberOfMapsBlocks = numberOfMapsBlocks + 1
        return numberOfMapsBlocks


    def getNumberOfDrawingAnimationBlocks(blocks, numberOfDrawingAnimationBlocks):
        for elem in blocks:
            if elem.attributes['type'].value == 'component_method':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in drawingAnimationComponents:
                            numberOfDrawingAnimationBlocks = numberOfDrawingAnimationBlocks + 1
            elif elem.attributes['type'].value == 'component_set_get':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in drawingAnimationComponents:
                            numberOfDrawingAnimationBlocks = numberOfDrawingAnimationBlocks + 1
            elif elem.attributes['type'].value == 'component_event':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in drawingAnimationComponents:
                            numberOfDrawingAnimationBlocks = numberOfDrawingAnimationBlocks + 1
        return numberOfDrawingAnimationBlocks


    def getNumberOfMediaBlocks(blocks, numberOfMediaBlocks):
        for elem in blocks:
            if elem.attributes['type'].value == 'component_method':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in mediaComponents:
                            numberOfMediaBlocks = numberOfMediaBlocks + 1
            elif elem.attributes['type'].value == 'component_set_get':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in mediaComponents:
                            numberOfMediaBlocks = numberOfMediaBlocks + 1
            elif elem.attributes['type'].value == 'component_event':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in mediaComponents:
                            numberOfMediaBlocks = numberOfMediaBlocks + 1
        return numberOfMediaBlocks


    def getNumberOfLayoutBlocks(blocks, numberOfLayoutBlocks):
        for elem in blocks:
            if elem.attributes['type'].value == 'component_method':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in layoutComponents:
                            numberOfLayoutBlocks = numberOfLayoutBlocks + 1
            elif elem.attributes['type'].value == 'component_set_get':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in layoutComponents:
                            numberOfLayoutBlocks = numberOfLayoutBlocks + 1
            elif elem.attributes['type'].value == 'component_event':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in layoutComponents:
                            numberOfLayoutBlocks = numberOfLayoutBlocks + 1
        return numberOfLayoutBlocks


    def getNumberOfUserInterfaceBlocks(blocks, numberOfUserInterfaceBlocks):
        for elem in blocks:
            if elem.attributes['type'].value == 'component_method':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in userInterfaceComponents:
                            numberOfUserInterfaceBlocks = numberOfUserInterfaceBlocks + 1
            elif elem.attributes['type'].value == 'component_set_get':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in userInterfaceComponents:
                            numberOfUserInterfaceBlocks = numberOfUserInterfaceBlocks + 1
            elif elem.attributes['type'].value == 'component_event':
                for elem2 in elem.getElementsByTagName('mutation'):
                    if elem2.hasAttribute('component_type'):
                        if elem2.attributes['component_type'].value in userInterfaceComponents:
                            numberOfUserInterfaceBlocks = numberOfUserInterfaceBlocks + 1
        return numberOfUserInterfaceBlocks


    def getNumberOfNoneCaseDefinedFunctionalBlocks(blocks, numberOfNoneCaseDefinedFunctionalBlocks, projectID, screenName, database):
        noneCaseFunctionalBlocks = 0

        for elem in blocks:
            if elem.attributes['type'].value == 'procedures_defreturn':
                for elem2 in elem.getElementsByTagName('field'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            value = elem2.firstChild.data
                            varName = value.replace('global ', '')
                            if re.fullmatch(snakeRegularExp, varName) == None and re.fullmatch(pascalRegularExp, varName) == None and re.fullmatch(camelCaseRegularExp, varName) == None:
                                noneCaseFunctionalBlocks = noneCaseFunctionalBlocks + 1
                                MySQLDataBase.insertIssue(projectID, screenName, varName, "procedures_defreturn", "NoneCaseDefinedFunctionalBlocks", database)
                for elem2 in elem.getElementsByTagName('title'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            value = elem2.firstChild.data
                            varName = value.replace('global ', '')
                            if re.fullmatch(snakeRegularExp, varName) == None and re.fullmatch(pascalRegularExp, varName) == None and re.fullmatch(camelCaseRegularExp, varName) == None:
                                noneCaseFunctionalBlocks = noneCaseFunctionalBlocks + 1
                                MySQLDataBase.insertIssue(projectID, screenName, varName, "procedures_defreturn", "NoneCaseDefinedFunctionalBlocks", database)

        for elem in blocks:
            if elem.attributes['type'].value == 'procedures_defnoreturn':
                for elem2 in elem.getElementsByTagName('field'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            value = elem2.firstChild.data
                            varName = value.replace('global ', '')
                            if re.fullmatch(snakeRegularExp, varName) == None and re.fullmatch(pascalRegularExp, varName) == None and re.fullmatch(camelCaseRegularExp, varName) == None:
                                noneCaseFunctionalBlocks = noneCaseFunctionalBlocks + 1
                                MySQLDataBase.insertIssue(projectID, screenName, varName, "procedures_defnoreturn", "NoneCaseDefinedFunctionalBlocks", database)
                for elem2 in elem.getElementsByTagName('title'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            value = elem2.firstChild.data
                            varName = value.replace('global ', '')
                            if re.fullmatch(snakeRegularExp, varName) == None and re.fullmatch(pascalRegularExp, varName) == None and re.fullmatch(camelCaseRegularExp, varName) == None:
                                noneCaseFunctionalBlocks = noneCaseFunctionalBlocks + 1
                                MySQLDataBase.insertIssue(projectID, screenName, varName, "procedures_defnoreturn", "NoneCaseDefinedFunctionalBlocks", database)

        numberOfNoneCaseDefinedFunctionalBlocks = numberOfNoneCaseDefinedFunctionalBlocks + noneCaseFunctionalBlocks
        return numberOfNoneCaseDefinedFunctionalBlocks


    def getNumberOfNoneCaseVariables(blocks, numberOfNoneCaseVariables, projectID, screenName, database):
        noneCaseVariables = 0

        for elem in blocks:
            if elem.attributes['type'].value == 'global_declaration':
                for elem2 in elem.getElementsByTagName('field'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            value = elem2.firstChild.data
                            varName = value.replace('global ', '')
                            if re.fullmatch(snakeRegularExp, varName) == None and re.fullmatch(pascalRegularExp, varName) == None and re.fullmatch(camelCaseRegularExp, varName) == None:
                                noneCaseVariables = noneCaseVariables + 1
                                MySQLDataBase.insertIssue(projectID, screenName, varName, "global_declaration", "NoneCaseVariables", database)

        for elem in blocks:
            if elem.attributes['type'].value == 'local_declaration_statement':
                for elem2 in elem.getElementsByTagName('localname'):
                    varName = elem2.attributes['name'].value
                    if re.fullmatch(snakeRegularExp, varName) == None and re.fullmatch(pascalRegularExp, varName) == None and re.fullmatch(camelCaseRegularExp, varName) == None:
                        noneCaseVariables = noneCaseVariables + 1
                        MySQLDataBase.insertIssue(projectID, screenName, varName, "local_declaration_statement", "NoneCaseVariables", database)
                    break

        for elem in blocks:
            if elem.attributes['type'].value == 'local_declaration_expression':
                for elem2 in elem.getElementsByTagName('localname'):
                    varName = elem2.attributes['name'].value
                    if re.fullmatch(snakeRegularExp, varName) == None and re.fullmatch(pascalRegularExp, varName) == None and re.fullmatch(camelCaseRegularExp, varName) == None:
                        noneCaseVariables = noneCaseVariables + 1
                        MySQLDataBase.insertIssue(projectID, screenName, varName, "local_declaration_expression", "NoneCaseVariables", database)
                    break

        numberOfNoneCaseVariables = numberOfNoneCaseVariables + noneCaseVariables
        return numberOfNoneCaseVariables


    def getNumberOfSnakeCaseDefinedFunctionalBlocks(blocks, numberOfSnakeCaseDefinedFunctionalBlocks, projectID, screenName, database):
        snakeCaseFunctionalBlocks = 0

        for elem in blocks:
            if elem.attributes['type'].value == 'procedures_defreturn':
                for elem2 in elem.getElementsByTagName('field'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            value = elem2.firstChild.data
                            varName = value.replace('global ', '')
                            if re.fullmatch(snakeRegularExp, varName) != None:
                                snakeCaseFunctionalBlocks = snakeCaseFunctionalBlocks + 1
                                MySQLDataBase.insertIssue(projectID, screenName, varName, "procedures_defreturn", "SnakeCaseDefinedFunctionalBlocks", database)
                for elem2 in elem.getElementsByTagName('title'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            value = elem2.firstChild.data
                            varName = value.replace('global ', '')
                            if re.fullmatch(snakeRegularExp, varName) != None:
                                snakeCaseFunctionalBlocks = snakeCaseFunctionalBlocks + 1
                                MySQLDataBase.insertIssue(projectID, screenName, varName, "procedures_defreturn", "SnakeCaseDefinedFunctionalBlocks", database)

        for elem in blocks:
            if elem.attributes['type'].value == 'procedures_defnoreturn':
                for elem2 in elem.getElementsByTagName('field'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            value = elem2.firstChild.data
                            varName = value.replace('global ', '')
                            if re.fullmatch(snakeRegularExp, varName) != None:
                                snakeCaseFunctionalBlocks = snakeCaseFunctionalBlocks + 1
                                MySQLDataBase.insertIssue(projectID, screenName, varName, "procedures_defnoreturn", "SnakeCaseDefinedFunctionalBlocks", database)
                for elem2 in elem.getElementsByTagName('title'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            value = elem2.firstChild.data
                            varName = value.replace('global ', '')
                            if re.fullmatch(snakeRegularExp, varName) != None:
                                snakeCaseFunctionalBlocks = snakeCaseFunctionalBlocks + 1
                                MySQLDataBase.insertIssue(projectID, screenName, varName, "procedures_defnoreturn", "SnakeCaseDefinedFunctionalBlocks", database)

        numberOfSnakeCaseDefinedFunctionalBlocks = numberOfSnakeCaseDefinedFunctionalBlocks + snakeCaseFunctionalBlocks
        return numberOfSnakeCaseDefinedFunctionalBlocks


    def getNumberOfSnakeCaseVariables(blocks, numberOfSnakeCaseVariables, projectID, screenName, database):
        snakeCaseVariables = 0

        for elem in blocks:
            if elem.attributes['type'].value == 'global_declaration':
                for elem2 in elem.getElementsByTagName('field'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            value = elem2.firstChild.data
                            varName = value.replace('global ', '')
                            if re.fullmatch(snakeRegularExp, varName) != None:
                                snakeCaseVariables = snakeCaseVariables + 1
                                MySQLDataBase.insertIssue(projectID, screenName, varName, "global_declaration", "SnakeCaseVariables", database)

        for elem in blocks:
            if elem.attributes['type'].value == 'local_declaration_statement':
                for elem2 in elem.getElementsByTagName('localname'):
                    varName = elem2.attributes['name'].value
                    if re.fullmatch(snakeRegularExp, varName) != None:
                        snakeCaseVariables = snakeCaseVariables + 1
                        MySQLDataBase.insertIssue(projectID, screenName, varName, "local_declaration_statement", "SnakeCaseVariables", database)
                    break

        for elem in blocks:
            if elem.attributes['type'].value == 'local_declaration_expression':
                for elem2 in elem.getElementsByTagName('localname'):
                    varName = elem2.attributes['name'].value
                    if re.fullmatch(snakeRegularExp, varName) != None:
                        snakeCaseVariables = snakeCaseVariables + 1
                        MySQLDataBase.insertIssue(projectID, screenName, varName, "local_declaration_expression", "SnakeCaseVariables", database)
                    break

        numberOfSnakeCaseVariables = numberOfSnakeCaseVariables + snakeCaseVariables
        return numberOfSnakeCaseVariables


    def getNumberOfPascalCaseDefinedFunctionalBlocks(blocks, numberOfPascalCaseDefinedFunctionalBlocks, projectID, screenName, database):
        pascalCaseFunctionalBlocks = 0

        for elem in blocks:
            if elem.attributes['type'].value == 'procedures_defreturn':
                for elem2 in elem.getElementsByTagName('field'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            value = elem2.firstChild.data
                            varName = value.replace('global ', '')
                            if re.fullmatch(pascalRegularExp, varName) != None:
                                pascalCaseFunctionalBlocks = pascalCaseFunctionalBlocks + 1
                                MySQLDataBase.insertIssue(projectID, screenName, varName, "procedures_defreturn", "PascalCaseDefinedFunctionalBlocks", database)
                for elem2 in elem.getElementsByTagName('title'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            value = elem2.firstChild.data
                            varName = value.replace('global ', '')
                            if re.fullmatch(pascalRegularExp, varName) != None:
                                pascalCaseFunctionalBlocks = pascalCaseFunctionalBlocks + 1
                                MySQLDataBase.insertIssue(projectID, screenName, varName, "procedures_defreturn", "PascalCaseDefinedFunctionalBlocks", database)

        for elem in blocks:
            if elem.attributes['type'].value == 'procedures_defnoreturn':
                for elem2 in elem.getElementsByTagName('field'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            value = elem2.firstChild.data
                            varName = value.replace('global ', '')
                            if re.fullmatch(pascalRegularExp, varName) != None:
                                pascalCaseFunctionalBlocks = pascalCaseFunctionalBlocks + 1
                                MySQLDataBase.insertIssue(projectID, screenName, varName, "procedures_defnoreturn", "PascalCaseDefinedFunctionalBlocks", database)
                for elem2 in elem.getElementsByTagName('title'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            value = elem2.firstChild.data
                            varName = value.replace('global ', '')
                            if re.fullmatch(pascalRegularExp, varName) != None:
                                pascalCaseFunctionalBlocks = pascalCaseFunctionalBlocks + 1
                                MySQLDataBase.insertIssue(projectID, screenName, varName, "procedures_defnoreturn", "PascalCaseDefinedFunctionalBlocks", database)

        numberOfPascalCaseDefinedFunctionalBlocks = numberOfPascalCaseDefinedFunctionalBlocks + pascalCaseFunctionalBlocks
        return numberOfPascalCaseDefinedFunctionalBlocks


    def getNumberOfPascalCaseVariables(blocks, numberOfPascalCaseVariables, projectID, screenName, database):
        pascalCaseVariables = 0

        for elem in blocks:
            if elem.attributes['type'].value == 'global_declaration':
                for elem2 in elem.getElementsByTagName('field'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            value = elem2.firstChild.data
                            varName = value.replace('global ', '')
                            if re.fullmatch(pascalRegularExp, varName) != None:
                                pascalCaseVariables = pascalCaseVariables + 1
                                MySQLDataBase.insertIssue(projectID, screenName, varName, "global_declaration", "PascalCaseVariables", database)

        for elem in blocks:
            if elem.attributes['type'].value == 'local_declaration_statement':
                for elem2 in elem.getElementsByTagName('localname'):
                    varName = elem2.attributes['name'].value
                    if re.fullmatch(pascalRegularExp, varName) != None:
                        pascalCaseVariables = pascalCaseVariables + 1
                        MySQLDataBase.insertIssue(projectID, screenName, varName, "local_declaration_statement", "PascalCaseVariables", database)
                    break

        for elem in blocks:
            if elem.attributes['type'].value == 'local_declaration_expression':
                for elem2 in elem.getElementsByTagName('localname'):
                    varName = elem2.attributes['name'].value
                    if re.fullmatch(pascalRegularExp, varName) != None:
                        pascalCaseVariables = pascalCaseVariables + 1
                        MySQLDataBase.insertIssue(projectID, screenName, varName, "local_declaration_expression", "PascalCaseVariables", database)
                    break

        numberOfPascalCaseVariables = numberOfPascalCaseVariables + pascalCaseVariables
        return numberOfPascalCaseVariables


    def getNumberOfCamelCaseDefinedFunctionalBlocks(blocks, numberOfCamelCaseDefinedFunctionalBlocks, projectID, screenName, database):
        camelCaseFunctionalBlocks = 0

        for elem in blocks:
            if elem.attributes['type'].value == 'procedures_defreturn':
                for elem2 in elem.getElementsByTagName('field'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            varName = elem2.firstChild.data
                            if re.fullmatch(camelCaseRegularExp, varName) != None:
                                camelCaseFunctionalBlocks = camelCaseFunctionalBlocks + 1
                                MySQLDataBase.insertIssue(projectID, screenName, varName, "procedures_defreturn", "CamelCaseDefinedFunctionalBlocks", database)
                for elem2 in elem.getElementsByTagName('title'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            varName = elem2.firstChild.data
                            if re.fullmatch(camelCaseRegularExp, varName) != None:
                                camelCaseFunctionalBlocks = camelCaseFunctionalBlocks + 1
                                MySQLDataBase.insertIssue(projectID, screenName, varName, "procedures_defreturn", "CamelCaseDefinedFunctionalBlocks", database)

        for elem in blocks:
            if elem.attributes['type'].value == 'procedures_defnoreturn':
                for elem2 in elem.getElementsByTagName('field'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            varName = elem2.firstChild.data
                            if re.fullmatch(camelCaseRegularExp, varName) != None:
                                camelCaseFunctionalBlocks = camelCaseFunctionalBlocks + 1
                                MySQLDataBase.insertIssue(projectID, screenName, varName, "procedures_defnoreturn", "CamelCaseDefinedFunctionalBlocks", database)
                for elem2 in elem.getElementsByTagName('title'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            varName = elem2.firstChild.data
                            if re.fullmatch(camelCaseRegularExp, varName) != None:
                                camelCaseFunctionalBlocks = camelCaseFunctionalBlocks + 1
                                MySQLDataBase.insertIssue(projectID, screenName, varName, "procedures_defnoreturn", "CamelCaseDefinedFunctionalBlocks", database)

        numberOfCamelCaseDefinedFunctionalBlocks = numberOfCamelCaseDefinedFunctionalBlocks + camelCaseFunctionalBlocks
        return numberOfCamelCaseDefinedFunctionalBlocks


    def getNumberOfCamelCaseVariables(blocks, numberOfCamelCaseVariables, projectID, screenName, database):
        camelCaseVariables = 0

        for elem in blocks:
            if elem.attributes['type'].value == 'global_declaration':
                for elem2 in elem.getElementsByTagName('field'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            value = elem2.firstChild.data
                            varName = value.replace('global ', '')
                            if re.fullmatch(camelCaseRegularExp, varName) != None:
                                camelCaseVariables = camelCaseVariables + 1
                                MySQLDataBase.insertIssue(projectID, screenName, varName, "global_declaration", "CamelCaseVariables", database)

        for elem in blocks:
            if elem.attributes['type'].value == 'local_declaration_statement':
                for elem2 in elem.getElementsByTagName('localname'):
                    varName = elem2.attributes['name'].value
                    if re.fullmatch(camelCaseRegularExp, varName) != None:
                        camelCaseVariables = camelCaseVariables + 1
                        MySQLDataBase.insertIssue(projectID, screenName, varName, "local_declaration_statement", "CamelCaseVariables", database)
                    break

        for elem in blocks:
            if elem.attributes['type'].value == 'local_declaration_expression':
                for elem2 in elem.getElementsByTagName('localname'):
                    varName = elem2.attributes['name'].value
                    if re.fullmatch(camelCaseRegularExp, varName) != None:
                        camelCaseVariables = camelCaseVariables + 1
                        MySQLDataBase.insertIssue(projectID, screenName, varName, "local_declaration_expression", "CamelCaseVariables", database)
                    break

        numberOfCamelCaseVariables = numberOfCamelCaseVariables + camelCaseVariables
        return numberOfCamelCaseVariables


    def getNumberOfVariablesInConditionNotUpdated(blocks, numberOfVariablesInConditionNotUpdated, projectID, screenName, database):
        conditionVars = []

        for elem in blocks:
            if elem.attributes['type'].value == 'controls_if':
                for elem2 in elem.getElementsByTagName('value'):
                    if 'IF' in elem2.attributes['name'].value:
                        for elem3 in elem2.getElementsByTagName('block'):
                            if elem3.attributes['type'].value == 'lexical_variable_get':
                                for elem4 in elem3.getElementsByTagName('field'):
                                    if elem4.attributes['name'].value == 'VAR':
                                        if elem4.firstChild != None:
                                            value = elem4.firstChild.data
                                            varName = value.replace('global ', '')
                                            if varName not in conditionVars:
                                                conditionVars.append(varName)
            if elem.attributes['type'].value == 'controls_while':
                for elem2 in elem.getElementsByTagName('value'):
                    if elem2.attributes['name'].value == 'TEST':
                        for elem3 in elem2.getElementsByTagName('block'):
                            if elem3.attributes['type'].value == 'lexical_variable_get':
                                for elem4 in elem3.getElementsByTagName('field'):
                                    if elem4.attributes['name'].value == 'VAR':
                                        if elem4.firstChild != None:
                                            value = elem4.firstChild.data
                                            varName = value.replace('global ', '')
                                            if varName not in conditionVars:
                                                conditionVars.append(varName)
            if elem.attributes['type'].value == 'controls_choose':
                for elem2 in elem.getElementsByTagName('value'):
                    if elem2.attributes['name'].value == 'TEST':
                        for elem3 in elem2.getElementsByTagName('block'):
                            if elem3.attributes['type'].value == 'lexical_variable_get':
                                for elem4 in elem3.getElementsByTagName('field'):
                                    if elem4.attributes['name'].value == 'VAR':
                                        if elem4.firstChild != None:
                                            value = elem4.firstChild.data
                                            varName = value.replace('global ', '')
                                            if varName not in conditionVars:
                                                conditionVars.append(varName)

        setsVars = []

        for elem in blocks:
            if elem.attributes['type'].value == 'lexical_variable_set':
                for elem2 in elem.getElementsByTagName('field'):
                    if elem2.attributes['name'].value == 'VAR':
                        if elem2.firstChild != None:
                            if elem2.firstChild.data not in setsVars:
                                value = elem2.firstChild.data
                                varName = value.replace('global ', '')
                                setsVars.append(varName)
                            break


        notifiedVars = []


        for elem in conditionVars:
            if elem not in setsVars:
                if elem not in notifiedVars:
                    notifiedVars.append(elem)
                    numberOfVariablesInConditionNotUpdated = numberOfVariablesInConditionNotUpdated + 1
                    MySQLDataBase.insertIssue(projectID, screenName, elem, "lexical_variable_get", "VariablesInConditionNotUpdated", database)

        return numberOfVariablesInConditionNotUpdated


    def getNumberOfWhileLoopsWithoutCondition(blocks, numberOfWhileLoopsWithoutCondition, projectID, screenName, database):
        whileBlocksWithoutCondition = 0
        hasCondition = False

        for elem in blocks:
            if elem.attributes['type'].value == 'controls_while':
                for elem2 in elem.getElementsByTagName('value'):
                    if elem2.attributes['name'].value == 'TEST':
                        hasCondition = True

                if hasCondition == False:
                    whileBlocksWithoutCondition = whileBlocksWithoutCondition + 1
                    MySQLDataBase.insertIssue(projectID, screenName, elem.attributes['id'].value, "controls_while", "WhileLoopsWithoutCondition", database)
                hasCondition = False

        numberOfWhileLoopsWithoutCondition = numberOfWhileLoopsWithoutCondition + whileBlocksWithoutCondition
        return numberOfWhileLoopsWithoutCondition


    def getNumberOfFunctionalBlocksWithoutReturn(blocks, numberOfFunctionalBlocksWithoutReturn, projectID, screenName, database):
        functionalBlocksWithoutReturn = 0
        hasReturn = False

        for elem in blocks:
            if elem.attributes['type'].value == 'procedures_defreturn':
                for elem2 in elem.getElementsByTagName('field'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            value = elem2.firstChild.data
                            varName = value.replace('global ', '')
                for elem2 in elem.getElementsByTagName('value'):
                    if elem2.attributes['name'].value == 'RETURN':
                        hasReturn = True

                if hasReturn == False:
                    functionalBlocksWithoutReturn = functionalBlocksWithoutReturn + 1
                    MySQLDataBase.insertIssue(projectID, screenName, varName, "procedures_defreturn", "FunctionalBlocksWithoutReturn", database)
                hasReturn = False

        numberOfFunctionalBlocksWithoutReturn = numberOfFunctionalBlocksWithoutReturn + functionalBlocksWithoutReturn
        return numberOfFunctionalBlocksWithoutReturn


    def getNumberOfDefinedFunctionalBlocksNotUsed(blocks, numberOfDefinedFunctionalBlocksNotUsed, projectID, screenName, database):
        definedFunctionalBlocks = []
        usedFuncionalBlocks = []
        proceduresDefReturn = []
        proceduresDefNoReturn = []

        for elem in blocks:
            if elem.attributes['type'].value == 'procedures_defreturn':
                for elem2 in elem.getElementsByTagName('field'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            value = elem2.firstChild.data
                            varName = value.replace('global ', '')
                            definedFunctionalBlocks.append(varName)
                            proceduresDefReturn.append(varName)
                for elem2 in elem.getElementsByTagName('title'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            value = elem2.firstChild.data
                            varName = value.replace('global ', '')
                            definedFunctionalBlocks.append(varName)
                            proceduresDefReturn.append(varName)
                

        for elem in blocks:
            if elem.attributes['type'].value == 'procedures_defnoreturn':
                for elem2 in elem.getElementsByTagName('field'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            value = elem2.firstChild.data
                            varName = value.replace('global ', '')
                            definedFunctionalBlocks.append(varName)
                            proceduresDefNoReturn.append(varName)
                for elem2 in elem.getElementsByTagName('title'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            value = elem2.firstChild.data
                            varName = value.replace('global ', '')
                            definedFunctionalBlocks.append(varName)
                            proceduresDefNoReturn.append(varName)

        for elem in blocks:
            if elem.attributes['type'].value == 'procedures_callnoreturn':
                for elem2 in elem.getElementsByTagName('field'):
                    if elem2.attributes['name'].value == 'PROCNAME':
                        if elem2.firstChild != None:
                            name = elem2.firstChild.data
                            if name not in usedFuncionalBlocks:
                                usedFuncionalBlocks.append(name)

        for elem in blocks:
            if elem.attributes['type'].value == 'procedures_callreturn':
                for elem2 in elem.getElementsByTagName('field'):
                    if elem2.attributes['name'].value == 'PROCNAME':
                        if elem2.firstChild != None:
                            name = elem2.firstChild.data
                            if name not in usedFuncionalBlocks:
                                usedFuncionalBlocks.append(name)

        if len(definedFunctionalBlocks) >= len(usedFuncionalBlocks):
            numberOfDefinedFunctionalBlocksNotUsed = numberOfDefinedFunctionalBlocksNotUsed + (len(definedFunctionalBlocks) - len(usedFuncionalBlocks))
        else: 
            numberOfDefinedFunctionalBlocksNotUsed = numberOfDefinedFunctionalBlocksNotUsed + 0

        for procedure in proceduresDefReturn:
            if procedure not in usedFuncionalBlocks:
                MySQLDataBase.insertIssue(projectID, screenName, procedure, "procedures_defreturn", "DefinedFunctionalBlocksNotUsed", database)

        for procedure in proceduresDefNoReturn:
            if procedure not in usedFuncionalBlocks:
                MySQLDataBase.insertIssue(projectID, screenName, procedure, "procedures_defnoreturn", "DefinedFunctionalBlocksNotUsed", database)


        return numberOfDefinedFunctionalBlocksNotUsed


    def getNumberOfDivisionByZero(blocks, numberOfDivisionByZero, projectID, screenName, database):
        divisionByZero = 0

        for elem in blocks:
            if elem.attributes['type'].value == 'math_division':
                for elem2 in elem.getElementsByTagName('value'):
                    if elem2.attributes['name'].value == 'B':
                        for elem3 in elem2.getElementsByTagName('block'):
                            if elem3.attributes['type'].value == 'math_number':
                                for elem4 in elem3.getElementsByTagName('field'):
                                    if elem4.attributes['name'].value == 'NUM':
                                        if elem4.firstChild != None:
                                            if elem4.firstChild.data == '0':
                                                divisionByZero = divisionByZero + 1
                                                MySQLDataBase.insertIssue(projectID, screenName, elem.attributes['id'].value, "math_division", "NumberOfDivisionByZero", database)

        numberOfDivisionByZero = numberOfDivisionByZero + divisionByZero
        return numberOfDivisionByZero


    def getNumberOfInfiniteLoops(blocks, numberOfInfiniteLoops, projectID, screenName, database):
        infiniteLoops = 0
        reportedInfiniteLoops = []

        #check loops with type of while(true)
        for elem in blocks:
            if elem.attributes['type'].value == 'controls_while':
                for elem2 in elem.getElementsByTagName('block'):
                    if elem2.attributes['type'].value == 'logic_boolean':
                        for elem3 in elem2.getElementsByTagName('field'):
                            if elem3.attributes['name'].value == 'BOOL':
                                if elem3.firstChild != None:
                                    if elem3.firstChild.data == 'TRUE':
                                        if elem not in reportedInfiniteLoops:
                                            reportedInfiniteLoops.append(elem)
                                            infiniteLoops = infiniteLoops + 1
                                            MySQLDataBase.insertIssue(projectID, screenName, elem.attributes['id'].value, "controls_while", "InfiniteLoops", database)

        #check loops with type while(a = a)
        for elem in blocks:
            a = 'without_value'
            b = 'without_value'
            EQ = False
            
            if elem.attributes['type'].value == 'controls_while':
                for elem2 in elem.getElementsByTagName('block'):
                    if elem2.attributes['type'].value == 'logic_compare':
                        for elem3 in elem2.getElementsByTagName('field'):
                            if elem3.attributes['name'].value == 'OP':
                                if elem3.firstChild != None:
                                    if elem3.firstChild.data == 'EQ':
                                        EQ = True
                        for elem3 in elem2.getElementsByTagName('value'):
                            if EQ == True:
                                if elem3.attributes['name'].value == 'A':
                                    for elem4 in elem3.getElementsByTagName('block'):
                                        if elem4.attributes['type'].value == 'math_number':
                                            for elem5 in elem4.getElementsByTagName('field'):
                                                if elem5.firstChild != None:
                                                    a = elem5.firstChild.data

                            if EQ == True:
                                if elem3.attributes['name'].value == 'B':
                                    for elem4 in elem3.getElementsByTagName('block'):
                                        if elem4.attributes['type'].value == 'math_number':
                                            for elem5 in elem4.getElementsByTagName('field'):
                                                if elem5.firstChild != None:
                                                    b = elem5.firstChild.data

                if EQ == True and a != 'without_value' and b != 'without_value':   
                    if a == b:
                        if elem not in reportedInfiniteLoops:
                            reportedInfiniteLoops.append(elem)
                            infiniteLoops = infiniteLoops + 1
                            MySQLDataBase.insertIssue(projectID, screenName, elem.attributes['id'].value, "controls_while", "InfiniteLoops", database)

        numberOfInfiniteLoops = numberOfInfiniteLoops + infiniteLoops
        return numberOfInfiniteLoops


    def getNumberOfVariablesNotInitialized(blocks, numberOfVariablesNotInitialized, projectID, screenName, database):
        varNotInitialized = 0

        for elem in blocks:
            if elem.attributes['type'].value == 'global_declaration':
                for elem2 in elem.getElementsByTagName('field'):
                    if elem2.attributes['name'].value == 'NAME':
                        if elem2.firstChild != None:
                            value = elem2.firstChild.data
                            varName = value.replace('global ', '')
                if len(elem.getElementsByTagName('value')) == 0:
                    varNotInitialized = varNotInitialized + 1
                    MySQLDataBase.insertIssue(projectID, screenName, varName, "global_declaration", "VariablesNotInitialized", database)

        for elem in blocks:
            if elem.attributes['type'].value == 'local_declaration_statement':
                for elem2 in elem.getElementsByTagName('localname'):
                    varName = elem2.attributes['name'].value
                    if len(elem.getElementsByTagName('value')) == 0:
                        varNotInitialized = varNotInitialized + 1
                        MySQLDataBase.insertIssue(projectID, screenName, varName, "local_declaration_statement", "VariablesNotInitialized", database)

        for elem in blocks:
            if elem.attributes['type'].value == 'local_declaration_expression':
                for elem2 in elem.getElementsByTagName('localname'):
                    varName = elem2.attributes['name'].value
                    if len(elem.getElementsByTagName('value')) == 0:
                        varNotInitialized = varNotInitialized + 1
                        MySQLDataBase.insertIssue(projectID, screenName, varName, "local_declaration_expression", "VariablesNotInitialized", database)

        numberOfVariablesNotInitialized = numberOfVariablesNotInitialized + varNotInitialized
        return numberOfVariablesNotInitialized


    def getNumberOfIndexOutOfRange(blocks, numberOfIndexOutOfRange, projectID, screenName, database):
        sizeOfLists = {}
        indexOutOfRange = 0
        varName = ''
        reportedIndexOutOfRange = []

        for elem in blocks:
            if elem.attributes['type'].value == 'lexical_variable_set':
                for elem2 in elem.getElementsByTagName('field'):
                    if elem2.hasAttribute('name'):
                        if elem2.attributes['name'].value == 'VAR':
                            if elem2.firstChild != None:
                                value = elem2.firstChild.data
                                varName = value.replace('global ', '')
                for elem2 in elem.getElementsByTagName('value'):
                    for elem3 in elem2.getElementsByTagName('block'):
                        if elem3.hasAttribute('type'):
                            if elem3.attributes['type'].value == 'lists_create_with':
                                for elem4 in elem3.getElementsByTagName('mutation'):
                                    if elem4.hasAttribute('items'):
                                        if varName != '':
                                            sizeOfLists[varName] = elem4.attributes['items'].value

        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'lists_select_item':
                    for elem2 in elem.getElementsByTagName('value'):
                        for elem3 in elem2.getElementsByTagName('block'):
                            if elem3.hasAttribute('type'):
                                if elem3.attributes['type'].value == 'lexical_variable_get':
                                    for elem4 in elem3.getElementsByTagName('field'):
                                        if elem4.hasAttribute('name'):
                                            if elem4.attributes['name'].value == 'VAR':
                                                if elem4.firstChild != None:
                                                    value = elem4.firstChild.data
                                                    varName = value.replace('global ', '')

                                if elem3.attributes['type'].value == 'math_number':
                                    for elem4 in elem3.getElementsByTagName('field'):
                                        if varName != '':
                                            if varName in sizeOfLists:
                                                if elem4.firstChild != None:
                                                    index = int(float(elem4.firstChild.data))
                                                    size = int(float(sizeOfLists[varName]))

                                                    if index > size:
                                                        if elem not in reportedIndexOutOfRange:
                                                            reportedIndexOutOfRange.append(elem)
                                                            indexOutOfRange = indexOutOfRange + 1
                                                            MySQLDataBase.insertIssue(projectID, screenName, elem.attributes['id'].value, "lists_select_item", "IndexOutOfRange", database)

        numberOfIndexOutOfRange = numberOfIndexOutOfRange + indexOutOfRange
        return numberOfIndexOutOfRange


    def getNumberOfDefinedFunctionalBlocks(blocks, numberOfDefinedFunctionalBlocks):
        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'procedures_defreturn':
                    numberOfDefinedFunctionalBlocks = numberOfDefinedFunctionalBlocks + 1

        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'procedures_defnoreturn':
                    numberOfDefinedFunctionalBlocks = numberOfDefinedFunctionalBlocks + 1
        return numberOfDefinedFunctionalBlocks


    def getNumberOfUsedFunctionalBlocks(blocks, numberOfUsedFunctionalBlocks):
        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'component_method':
                    numberOfUsedFunctionalBlocks = numberOfUsedFunctionalBlocks + 1

        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'procedures_callnoreturn':
                    numberOfUsedFunctionalBlocks = numberOfUsedFunctionalBlocks + 1

        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'procedures_callreturn':
                    numberOfUsedFunctionalBlocks = numberOfUsedFunctionalBlocks + 1
        return numberOfUsedFunctionalBlocks


    def getNumberOfEventsBlocks(blocks, numberOfEventsBlocks):
        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'component_event':
                    numberOfEventsBlocks = numberOfEventsBlocks + 1
        return numberOfEventsBlocks


    def getNumberOfConditionalBlocks(blocks, numberOfConditionalBlocks):
        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'controls_if':
                    numberOfConditionalBlocks = numberOfConditionalBlocks + 1

        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'controls_choose':
                    numberOfConditionalBlocks = numberOfConditionalBlocks + 1
        return numberOfConditionalBlocks


    def getNumberOfLoopsBlocks(blocks, numberOfLoopsBlocks):
        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'controls_while':
                    numberOfLoopsBlocks = numberOfLoopsBlocks + 1

        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'controls_forRange':
                    numberOfLoopsBlocks = numberOfLoopsBlocks + 1

        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'controls_for_each_dict':
                    numberOfLoopsBlocks = numberOfLoopsBlocks + 1

        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'controls_do_then_return':
                    numberOfLoopsBlocks = numberOfLoopsBlocks + 1
        return numberOfLoopsBlocks


    def getNumberOfGlobalVariables(blocks, numberOfGlobalVariables):
        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'global_declaration':
                    for elem2 in elem.getElementsByTagName('field'):
                        if elem2.attributes['name'].value == 'NAME':
                            numberOfGlobalVariables = numberOfGlobalVariables + 1
        return numberOfGlobalVariables


    def getNumberOfLocalVariables(blocks, numberOfLocalVariables):
        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'local_declaration_statement':
                    for elem2 in elem.getElementsByTagName('localname'):
                        numberOfLocalVariables = numberOfLocalVariables + 1
                        break

        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'local_declaration_expression':
                    for elem2 in elem.getElementsByTagName('localname'):
                        numberOfLocalVariables = numberOfLocalVariables + 1
                        break
        return numberOfLocalVariables


    def getNumberOfScreensError(numberOfScreens, projectID, screenName, database):
        if numberOfScreens > 10:
            MySQLDataBase.insertIssue(projectID, screenName, screenName, "Screen", "NumberOfScreensError", database)
            return 1
        else:
            return 0


    def removeUniqueTags(block):

        blockString = str(block.toxml())
        regularExp = r'id=".[^"]+"'
        blockString = re.sub(regularExp, 'id=""', blockString)

        regularExp = r'x=".[^"]+"'
        blockString = re.sub(regularExp, 'x=""', blockString)

        regularExp = r'y=".[^"]+"'
        blockString = re.sub(regularExp, 'y=""', blockString)

        regularExp = r'<field name="NAME">.[^"]+</field>'
        blockString = re.sub(regularExp, '<field name="NAME"></field>', blockString)

        regularExp = r'instance_name=".[^"]+"'
        blockString = re.sub(regularExp, 'instance_name=""', blockString)

        regularExp = r'<comment.[^<]+</comment>'
        blockString = re.sub(regularExp, '<comment></comment>', blockString)

        block = parseString(blockString)

        return block

    def getDuplicateBlocks(blocks):
        duplicateBlocks = []
        processedBlocks = []
        blocksToAnalyze = ['procedures_defreturn', 'procedures_defnoreturn', 'controls_if', 'controls_choose', 'controls_while',' controls_forRange', 'controls_for_each_dict', 'controls_do_then_return']
        analyzedBlocks = 0

        for elem in blocks:
            #borramos los campos únicos
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value in blocksToAnalyze:
                    analyzedBlocks = analyzedBlocks + 1
                    processedBlocks.append(AppInventorMetrics.removeUniqueTags(elem))

        for index, elem in enumerate(processedBlocks):
            for index2, elem2 in enumerate(processedBlocks):
                if(elem not in duplicateBlocks) and (elem2 not in duplicateBlocks):
                    if (index != index2) and elem.toxml() == elem2.toxml():
                        parent = elem.parentNode
                        if (elem not in duplicateBlocks) and (parent not in duplicateBlocks):
                            duplicateBlocks.append(elem)
        return duplicateBlocks, analyzedBlocks


    def getNumberOfDuplicateBlocks(blocks, numberOfDuplicateBlocks, numberOfAnalyzedBlocks):
        duplicateBlocks, analyzedBlocks = AppInventorMetrics.getDuplicateBlocks(blocks)

        return numberOfDuplicateBlocks + len(duplicateBlocks), numberOfAnalyzedBlocks + analyzedBlocks


    def getVariablesWithNamesTooShorts(blocks, errorsVariablesNames, projectID, screenName, database):
        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'global_declaration':
                    for elem2 in elem.getElementsByTagName('field'):
                        if elem2.attributes['name'].value == 'NAME':
                            if elem2.firstChild != None:
                                value = elem2.firstChild.data
                                varName = value.replace('global ', '')
                                if len(varName) < 3:
                                    errorsVariablesNames.append(varName)
                                    MySQLDataBase.insertIssue(projectID, screenName, varName, "global_declaration", "NameOfVariablesErrors", database)

        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'local_declaration_statement':
                    for elem2 in elem.getElementsByTagName('localname'):
                        varName = elem2.attributes['name'].value
                        if len(varName) < 3:
                            errorsVariablesNames.append(varName)
                            MySQLDataBase.insertIssue(projectID, screenName, varName, "local_declaration_statement", "NameOfVariablesErrors", database)
                        break

        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'local_declaration_expression':
                    for elem2 in elem.getElementsByTagName('localname'):
                        varName = elem2.attributes['name'].value
                        if len(varName) < 3:
                            errorsVariablesNames.append(varName)
                            MySQLDataBase.insertIssue(projectID, screenName, varName, "local_declaration_expression", "NameOfVariablesErrors", database)
                        break
        return errorsVariablesNames


    def getFunctionsWithNamesTooShorts(blocks, errorsFunctionsNames, projectID, screenName, database):
        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'procedures_defreturn':
                    for elem2 in elem.getElementsByTagName('field'):
                        if elem2.attributes['name'].value == 'NAME':
                            if elem2.firstChild != None:
                                value = elem2.firstChild.data
                                varName = value.replace('global ', '')
                                if len(varName) < 3:
                                    errorsFunctionsNames.append(varName)
                                    MySQLDataBase.insertIssue(projectID, screenName, varName, "procedures_defreturn", "NameOfFunctionsErrors", database)

                    for elem2 in elem.getElementsByTagName('title'):
                        if elem2.attributes['name'].value == 'NAME':
                            if elem2.firstChild != None:
                                value = elem2.firstChild.data
                                varName = value.replace('global ', '')
                                if len(varName) < 3:
                                    errorsFunctionsNames.append(varName)
                                    MySQLDataBase.insertIssue(projectID, screenName, varName, "procedures_defreturn", "NameOfFunctionsErrors", database)

        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'procedures_defnoreturn':
                    for elem2 in elem.getElementsByTagName('field'):
                        if elem2.attributes['name'].value == 'NAME':
                            if elem2.firstChild != None:
                                value = elem2.firstChild.data
                                varName = value.replace('global ', '')
                                if len(varName) < 3:
                                    errorsFunctionsNames.append(varName)
                                    MySQLDataBase.insertIssue(projectID, screenName, varName, "procedures_defnoreturn", "NameOfFunctionsErrors", database)

                    for elem2 in elem.getElementsByTagName('title'):
                        if elem2.attributes['name'].value == 'NAME':
                            if elem2.firstChild != None:
                                value = elem2.firstChild.data
                                varName = value.replace('global ', '')
                                if len(varName) < 3:
                                    errorsFunctionsNames.append(varName)
                                    MySQLDataBase.insertIssue(projectID, screenName, varName, "procedures_defnoreturn", "NameOfFunctionsErrors", database)
        return errorsFunctionsNames


    def getFunctionsWithTooManyParameters(blocks, errorsNumberOfArguments, projectID, screenName, database):
        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'procedures_defreturn':
                    if len(elem.getElementsByTagName('arg')) > 3:
                        errorsNumberOfArguments = errorsNumberOfArguments + 1
                        for elem2 in elem.getElementsByTagName('field'):
                            if elem2.attributes['name'].value == 'NAME':
                                if elem2.firstChild != None:
                                    value = elem2.firstChild.data
                                    varName = value.replace('global ', '')
                                    MySQLDataBase.insertIssue(projectID, screenName, varName, "procedures_defreturn", "FunctionsWithTooManyParameters", database)

        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'procedures_defnoreturn':
                    if len(elem.getElementsByTagName('arg')) > 3:
                        errorsNumberOfArguments = errorsNumberOfArguments + 1
                        for elem2 in elem.getElementsByTagName('field'):
                            if elem2.attributes['name'].value == 'NAME':
                                if elem2.firstChild != None:
                                    value = elem2.firstChild.data
                                    varName = value.replace('global ', '')
                                    MySQLDataBase.insertIssue(projectID, screenName, varName, "procedures_defnoreturn", "FunctionsWithTooManyParameters", database)
        return errorsNumberOfArguments


    def getVariablesNotUsed(blocks, errorsValuesNotUsed, projectID, screenName, database):
        globalVars = []
        localVarsStatement = []
        localVarsExpression = []

        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'global_declaration':
                    for elem2 in elem.getElementsByTagName('field'):
                        if elem2.attributes['name'].value == 'NAME':
                            if elem2.firstChild != None:
                                value = elem2.firstChild.data
                                varName = value.replace('global ', '')
                                globalVars.append(varName)

        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'local_declaration_statement':
                    for elem2 in elem.getElementsByTagName('localname'):
                        varName = elem2.attributes['name'].value
                        localVarsStatement.append(varName)
                        break

        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'local_declaration_expression':
                    for elem2 in elem.getElementsByTagName('localname'):
                        varName = elem2.attributes['name'].value
                        localVarsExpression.append(varName)
                        break

        setsVars = []

        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'lexical_variable_set':
                    for elem2 in elem.getElementsByTagName('field'):
                        if elem2.attributes['name'].value == 'VAR':
                            if elem2.firstChild != None:
                                if elem2.firstChild.data not in setsVars:
                                    value = elem2.firstChild.data
                                    varName = value.replace('global ', '')
                                    setsVars.append(varName)

        getsVars = []

        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'lexical_variable_get':
                    for elem2 in elem.getElementsByTagName('field'):
                        if elem2.attributes['name'].value == 'VAR':
                            if elem2.firstChild != None:
                                if elem2.firstChild.data not in getsVars:
                                    value = elem2.firstChild.data
                                    varName = value.replace('global ', '')
                                    getsVars.append(varName)


        for elem in globalVars:
            if elem not in getsVars and elem not in setsVars:
                errorsValuesNotUsed = errorsValuesNotUsed + 1
                MySQLDataBase.insertIssue(projectID, screenName, elem, "global_declaration", "VariablesNotUsed", database)

        for elem in localVarsStatement:
            if elem not in getsVars and elem not in setsVars:
                errorsValuesNotUsed = errorsValuesNotUsed + 1
                MySQLDataBase.insertIssue(projectID, screenName, elem, "local_declaration_statement", "VariablesNotUsed", database)

        for elem in localVarsExpression:
            if elem not in getsVars and elem not in setsVars:
                errorsValuesNotUsed = errorsValuesNotUsed + 1
                MySQLDataBase.insertIssue(projectID, screenName, elem, "local_declaration_expression", "VariablesNotUsed", database)

        return errorsValuesNotUsed


    def getNumberOfComments(comments, numberOfComments):
        return numberOfComments + len(comments)


    def getMagicNumbers(blocks, magicNumbers, projectID, screenName, database):
        numbers = []
        assignedNumbers = []

        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'math_number':
                    for elem2 in elem.getElementsByTagName('field'):
                        if elem2.attributes['name'].value == 'NUM':
                            if elem2.firstChild != None:
                                numbers.append(elem2.firstChild.data)
                if elem.attributes['type'].value == 'global_declaration':
                    for elem2 in elem.getElementsByTagName('block'):
                        if elem2.attributes['type'].value == 'math_number':
                            for elem3 in elem2.getElementsByTagName('field'):
                                if elem3.attributes['name'].value == 'NUM':
                                    if elem3.firstChild != None:
                                        assignedNumbers.append(elem3.firstChild.data)
                if elem.attributes['type'].value == 'local_declaration_statement':
                    for elem2 in elem.getElementsByTagName('block'):
                        if elem2.attributes['type'].value == 'math_number':
                            for elem3 in elem2.getElementsByTagName('field'):
                                if elem3.attributes['name'].value == 'NUM':
                                    if elem3.firstChild != None:
                                        assignedNumbers.append(elem3.firstChild.data)
                if elem.attributes['type'].value == 'local_declaration_expression':
                    for elem2 in elem.getElementsByTagName('block'):
                        if elem2.attributes['type'].value == 'math_number':
                            for elem3 in elem2.getElementsByTagName('field'):
                                if elem3.attributes['name'].value == 'NUM':
                                    if elem3.firstChild != None:
                                        assignedNumbers.append(elem3.firstChild.data)
                if elem.attributes['type'].value == 'lexical_variable_set':
                    for elem2 in elem.getElementsByTagName('block'):
                        if elem2.attributes['type'].value == 'math_number':
                            for elem3 in elem2.getElementsByTagName('field'):
                                if elem3.attributes['name'].value == 'NUM':
                                    if elem3.firstChild != None:
                                        assignedNumbers.append(elem3.firstChild.data)
                if elem.attributes['type'].value == 'component_set_get':
                    for elem2 in elem.getElementsByTagName('block'):
                        if elem2.attributes['type'].value == 'math_number':
                            for elem3 in elem2.getElementsByTagName('field'):
                                if elem3.attributes['name'].value == 'NUM':
                                    if elem3.firstChild != None:
                                        assignedNumbers.append(elem3.firstChild.data)
        if len(numbers) >= len(assignedNumbers):
            magicNumbers = magicNumbers + (len(numbers) - len(assignedNumbers))
        else:
            magicNumbers = magicNumbers + 0

        reportedNumbers = []

        for number in numbers:
            if number not in assignedNumbers:
                if number not in reportedNumbers:
                    reportedNumbers.append(number)
                    MySQLDataBase.insertIssue(projectID, screenName, number, "math_number", "MagicNumbers", database)

        return magicNumbers


    def getFunctionsWithTooManyBlocks(blocks, numberOfFunctionsWithTooManyBlocks, projectID, screenName, database):
        composeBlocks = ['procedures_defreturn', 'procedures_defnoreturn', 'controls_if', 'controls_while',' controls_forRange']
        blocksToCount = ['procedures_defreturn', 'procedures_defnoreturn', 'controls_if', 'controls_while',' controls_forRange', 'component_set_get', 'lexical_variable_set', 'lexical_variable_get']
        functionsWithTooManyBlocks = []
        numberOfBlocks = 0

        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'procedures_defreturn' or elem.attributes['type'].value == 'procedures_defnoreturn':
                    for elem2 in elem.getElementsByTagName('block'):
                        if elem2.attributes['type'].value in blocksToCount:
                            numberOfBlocks = numberOfBlocks + 1
                    if numberOfBlocks > 15:
                        functionsWithTooManyBlocks.append(elem)
                        for elem2 in elem.getElementsByTagName('field'):
                            if elem2.attributes['name'].value == 'NAME':
                                if elem2.firstChild != None:
                                    value = elem2.firstChild.data
                                    varName = value.replace('global ', '')
                                    MySQLDataBase.insertIssue(projectID, screenName, varName, elem.attributes['type'].value, "FunctionsWithTooManyBlocks", database)
                    numberOfBlocks = 0  

        numberOfFunctionsWithTooManyBlocks = numberOfFunctionsWithTooManyBlocks + len(functionsWithTooManyBlocks) 
        return numberOfFunctionsWithTooManyBlocks


    def getIfBlocksTooManyNested(blocks, ifBlocksTooManyNested, projectID, screenName, database):
        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'controls_if': #base level
                    for elem2 in elem.getElementsByTagName('block'):
                        if elem2.hasAttribute('type'):
                            if elem2.attributes['type'].value == 'controls_if': #first level
                                for elem3 in elem2.getElementsByTagName('block'):
                                    if elem3.hasAttribute('type'):
                                        if elem3.attributes['type'].value == 'controls_if': #second level
                                            if elem not in ifBlocksTooManyNested:
                                                ifBlocksTooManyNested.append(elem)
                                                MySQLDataBase.insertIssue(projectID, screenName, elem.attributes['id'].value, "controls_if", "IfBlocksTooManyNested", database)

        return ifBlocksTooManyNested


    def getCiclomaticComplexityPerFunction(blocks):
        ciclomaticComplexityResult = []
        ciclomaticComplexity = 0
        evaluatorsBlocks = ['controls_if', 'controls_while', 'controls_forRange']
        evaluateBlocks = []

        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'procedures_defreturn':
                    ciclomaticComplexity = 1
                    for elem2 in elem.getElementsByTagName('block'):
                        if (elem2.attributes['type'].value in evaluatorsBlocks) and (elem2 not in evaluateBlocks):
                            ciclomaticComplexity = ciclomaticComplexity + 1
                            evaluateBlocks.append(elem2)
                    ciclomaticComplexityResult.append(ciclomaticComplexity)
                    ciclomaticComplexity = 0
                    evaluateBlocks = []

        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'procedures_defnoreturn':
                    ciclomaticComplexity = 1
                    for elem2 in elem.getElementsByTagName('block'):
                        if (elem2.attributes['type'].value in evaluatorsBlocks) and (elem2 not in evaluateBlocks):
                            ciclomaticComplexity = ciclomaticComplexity + 1
                            evaluateBlocks.append(elem2)
                    ciclomaticComplexityResult.append(ciclomaticComplexity)
                    ciclomaticComplexity = 0
                    evaluateBlocks = []

        return ciclomaticComplexityResult


    def getCognitiveComplexityPerFunction(blocks):
        cognitiveComplexityResult = []
        cognitiveComplexity = 0
        countedBlocks = []
        evaluatorsblocks = ['controls_if', 'controls_while', 'controls_forRange']

        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'procedures_defreturn':
                    cognitiveComplexity = 1
                    for elem2 in elem.getElementsByTagName('block'):
                        #base level (+1)
                        if elem2.hasAttribute('type'):
                            if elem2.attributes['type'].value in evaluatorsblocks:
                                if elem2 not in countedBlocks:
                                    cognitiveComplexity = cognitiveComplexity + 1
                                    countedBlocks.append(elem2)
                            for elem3 in elem2.getElementsByTagName('block'):
                                #first level (+2)
                                if elem3.hasAttribute('type'):
                                    if elem3.attributes['type'].value in evaluatorsblocks:
                                        if elem3 not in countedBlocks:
                                            cognitiveComplexity = cognitiveComplexity + 2
                                            countedBlocks.append(elem3)
                                    for elem4 in elem3.getElementsByTagName('block'):
                                        #second level (+3)
                                        if elem4.hasAttribute('type'):
                                            if elem4.attributes['type'].value in evaluatorsblocks:
                                                if elem4 not in countedBlocks:
                                                    cognitiveComplexity = cognitiveComplexity + 3
                                                    countedBlocks.append(elem4)
                                            for elem5 in elem4.getElementsByTagName('block'):
                                                #third level (+4)
                                                if elem5.hasAttribute('type'):
                                                    if elem5.attributes['type'].value in evaluatorsblocks:
                                                        if elem5 not in countedBlocks:
                                                            cognitiveComplexity = cognitiveComplexity + 4
                                                            countedBlocks.append(elem5)
                    cognitiveComplexityResult.append(cognitiveComplexity)
                    countedBlocks = []
                    cognitiveComplexity = 0

        for elem in blocks:
            if elem.hasAttribute('type'):
                if elem.attributes['type'].value == 'procedures_defnoreturn':
                    cognitiveComplexity = 1
                    for elem2 in elem.getElementsByTagName('block'):
                        #base level (+1)
                        if elem2.hasAttribute('type'):
                            if elem2.attributes['type'].value in evaluatorsblocks:
                                if elem2 not in countedBlocks:
                                    cognitiveComplexity = cognitiveComplexity + 1
                                    countedBlocks.append(elem2)
                            for elem3 in elem2.getElementsByTagName('block'):
                                #first level (+2)
                                if elem3.hasAttribute('type'):
                                    if elem3.attributes['type'].value in evaluatorsblocks:
                                        if elem3 not in countedBlocks:
                                            cognitiveComplexity = cognitiveComplexity + 2
                                            countedBlocks.append(elem3)
                                    for elem4 in elem3.getElementsByTagName('block'):
                                        #second level (+3)
                                        if elem4.hasAttribute('type'):
                                            if elem4.attributes['type'].value in evaluatorsblocks:
                                                if elem4 not in countedBlocks:
                                                    cognitiveComplexity = cognitiveComplexity + 3
                                                    countedBlocks.append(elem4)
                                            for elem5 in elem4.getElementsByTagName('block'):
                                                #third level (+4)
                                                if elem5.hasAttribute('type'):
                                                    if elem5.attributes['type'].value in evaluatorsblocks:
                                                        if elem5 not in countedBlocks:
                                                            cognitiveComplexity = cognitiveComplexity + 4
                                                            countedBlocks.append(elem5)
                    cognitiveComplexityResult.append(cognitiveComplexity)
                    countedBlocks = []
                    cognitiveComplexity = 0

        return cognitiveComplexityResult