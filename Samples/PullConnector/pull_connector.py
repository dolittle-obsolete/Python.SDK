#---------------------------------------------------------------------------------------------
#  Copyright (c) Dolittle. All rights reserved.
#  Licensed under the MIT License. See LICENSE in the project root for license information.
#---------------------------------------------------------------------------------------------
#from '../../Source/Connectors/PullConnector' import PullConnector

# https://pdoc3.github.io/pdoc/
# https://pdoc3.github.io/pdoc/doc/pdoc/

class TagDataPoint():
    """Represents an unidentified data point"""
    tag = ''
    value = 0

class IAmAPullConnector():
    """Pretends its an interface for a pull connector"""
    def pull(self):
        return []

class PullConnector(IAmAPullConnector):
    def __init__(self):
        print("Hello world")

    def pull(self):
        return [TagDataPoint()]
