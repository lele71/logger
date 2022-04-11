class Logger:
    def __init__(self, position, appName, level='noset'):
        self.position = position
        self.appName = appName
        self.currentFilter=[0]
        self.lastError = ''
        self.availableFilter = {
            0: 'NOSET',
            10: 'DEBUG',
            20: 'INFO',
            30: 'WARNING',
            40: 'ERROR',
            50: 'CRITICAL',
            100: 'TOSTDOUT'
        }
    
    # private get datetine like string
    def __datetime(self):
        from datetime import datetime
        now = datetime.now()
        nowString = now.strftime("%Y-%m-%d %H:%M:%S.%f")
        return nowString
    
    # private get datetine like string
    def __date(self):
        from datetime import datetime
        now = datetime.now()
        nowString = now.strftime("%Y-%m-%d")
        return nowString
    
    # private method to write to file or stdout
    def __writeLog(self, message):
        f = "%s%s-%s.log"%(self.position, self.__date(), self.appName)
        try:
            ff = open(f, "a")
            ff.write("%s\n"%message)
            ff.close
        except Exception as e:
            self.lastError = e
            return False
        return True
        
        print("Filename: %s"%f)
        print(message)
        
    # Return the last error    
    def getLastError(self):
        return self.lastError
    
    # Return list of filters
    def getFilter(self):
        return self.currentFilter
    
    # return available filter
    def getAvailableFilter(self):
        return self.availableFilter
    
    # Add a filter ti list if not present
    def addFilter(self, filterList):
        error = False
        for f in filterList:
            if type(f) == int:
                # is int
                # check if filter exist
                if f in self.availableFilter:
                    # check if filter is not already in list
                    if not f in self.currentFilter:
                        # not il list append
                        self.currentFilter.append(f)
                    else:
                        # already in list error
                        self.lastError += "%s already in list\n"%str(f)
                        error = True
                else:
                    # not in available filter error
                    self.lastError += "%s not in available filter\n"%str(f)
                    error = True
            elif type(f) == str:
                # is str
                # check filter code
                filterExist = False
                for j in self.availableFilter:
                    # check if in available filter
                    if f.upper() == self.availableFilter[j]:
                        filterExist = True
                        # check if filter is not already in list
                        if not f in self.currentFilter:
                            # not il list append
                            self.currentFilter.append(j)
                        else:
                            # already in list error
                            self.lastError += "%s already in list\n"%str(f)
                            error = True
                if filterExist:
                    error = False
                else:  
                    # not in available filter error
                    self.lastError += "%s not in available filter\n"%str(f)              
            else:
                # not int or str error
                self.lastError += "%s not correct format\n"%str(f)
                error = True
        return not error
    
    def removeFilter(self, filters):
        for filter in filters:
            # filter is int
            if type(filter) == int:
                # check if is in availableFilter
                try:
                    text = self.availableFilter[filter]
                except:
                    self.lastError += "%s not in available filter\n"%str(filter)
                    return False
                # delete from list
                try:
                    self.currentFilter.remove(filter)
                except:
                    self.lastError += "%s not in filter list\n"%str(filter)
            elif type(filter) == str:
                # filter is string
                # try to get filter code
                filterCode = -1
                for j in self.availableFilter:
                    # check if in available filter
                    if filter.upper() == self.availableFilter[j]:
                        filterCode = j
                if filterCode == -1:
                    # not find in availableFilter
                    self.lastError += "%s not in available filter\n"%str(filter)
                    return False
                # here I find a correct code
                # delete from list
                try:
                    self.currentFilter.remove(filterCode)
                except:
                    self.lastError += "%s not in filter list\n"%str(filter)
                    return False
            else:
                # not int or str error
                self.lastError += "%s not correct format\n"%str(filter)
                return False
        return True
    
    def log(self, level, msg, timestamp="None"):
        error = False
        # check if log is filtred
        # case level is int
        if type(level) == int:
            # int provided
            # check if level exist
            if level in self.availableFilter:
                # check if level is filtered
                if level not in self.currentFilter:
                    # level not filtered write log
                    levelTxt = self.availableFilter[level]
                    # check if timestamp is provided
                    if timestamp != "None":
                        now = timestamp
                    else:
                        now = self.__datetime()
                    message = "%s from %s <%s> %s"%(now, self.appName, levelTxt, msg)
                    if not self.__writeLog(message):
                        return False    
                else:
                    # log filtered for now only pass
                    pass
            else:
                # not in available filter error
                self.lastError += "%s not in available filter\n"%str(level)
                error = True 
        elif type(level) ==  str:
            filterExist = False
            for j in self.availableFilter:
                # check if in available filter
                if level.upper() == self.availableFilter[j]:
                    # exist in available filter
                    filterExist = True
                    print("TROVATO")
                    # check if is filtered
                    if level not in self.currentFilter:
                        # level not filtered write log
                        # check if timestamp is provided
                        if timestamp != "None":
                            now = timestamp
                        else:
                            now = self.__datetime()
                        message = "%s from %s <%s> %s"%(now, self.appName, level.upper(), msg)
                        if not self.__writeLog(message):
                            return False
                    else:
                        # log filtered for now only pass
                        pass 
            if filterExist:
                error = False
            else:  
                # not in available filter error
                self.lastError += "%s not in available filter\n"%str(level)
                error = True
        else:
            # no int or str provided
            self.lastError += "%s not correct format\n"%str(level)
            error = True
        return not error