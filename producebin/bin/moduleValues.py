#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time: 2018-08-10

import time
from producebin.dbpObject import DBPObject

class ModuleValues(DBPObject):

    # 各个导出类型模块的总的生成数据的方法

    def __init__(self, valuesObj):

        self.valuesObj = valuesObj



    def mdGenerate(self, exportMDObj, strDBName, strTableName):

        # md模块的外接方法
        # exportMDObj: exportMD对象
        # strDBName: 库名, string类型
        # strTableName: 表名字, string类型
        # 执行完成返回1, 否则返回-1

        intIndexTime = time.time()

        try:

            exportMDObj.writerTitle(strTableName)

            listDictTableChangeMsg = self.valuesObj.getSingleTableChangeMsg(strDBName, strTableName)

            if listDictTableChangeMsg is not None:

                exportMDObj.writerTable(listDictTableChangeMsg)

                listDictResultObj = self.valuesObj.getSingleTableMsg(strDBName, strTableName)

                if listDictResultObj is not None:

                    exportMDObj.writerTable(listDictResultObj)
                else:
                    self.logUtilObj.writerLog('未获取到表' + strTableName + '的信息')
                    return -1

            else:
                self.logUtilObj.writerLog('未获取到表' + strTableName + '的历史更改信息')
                return -1

        except Exception as error:
            intResult = -1
            self.logUtilObj.writerLog(str(error))
            return intResult

        return 1


    def mdGenerateTuple(self, exportMDObj, strDBName, tupleTableName):

        # md模块的外接方法
        # exportMDObj: exportMD对象
        # strDBName: 库名, string类型
        # tupleTableName: 表名字, tuple元组类型/或者list
        # 执行完成返回1, 否则返回-1

        intIndexTime = time.time()
        intIndex = 0

        for strTableName in tupleTableName:

            try:

                exportMDObj.writerTitle(strTableName)

                listDictTableChangeMsg = self.valuesObj.getSingleTableChangeMsg(strDBName, strTableName)

                if listDictTableChangeMsg is not None:
                    exportMDObj.writerTable(listDictTableChangeMsg)

                    listDictResultObj = self.valuesObj.getSingleTableMsg(strDBName, strTableName)

                    if listDictResultObj is not None:

                        intIndex = exportMDObj.writerTable(listDictResultObj)

                        if intIndex == -1:
                            self.logUtilObj.writerLog(strDBName + '.' + strTableName + ' 导出出错')
                        else:
                            self.logUtilObj.writerLog(strDBName + '.' + strTableName + ' 导出成功')
                    else:
                        self.logUtilObj.writerLog('未获取到表' + strTableName + '信息')
                else:
                    self.logUtilObj.writerLog('未获取到表' + strTableName + '的历史更改信息')


            except Exception as error:
                self.logUtilObj.writerLog(strDBName + '.' + strTableName + ' 导出出错')
                self.logUtilObj.writerLog(str(error))
                intIndex = -1
        if intIndex != 1:
            self.logUtilObj.writerLog('=====导出出错=====')
            self.logUtilObj.writerLog('详情请看日志: ' + self.logUtilObj.strLogFileName)
            intResult = -1

        else:
            self.logUtilObj.writerLog('=====导出完成=====')
            self.logUtilObj.writerLog('导出文件路径: ' + exportMDObj.strFileName)
            intResult = 1

        self.logUtilObj.writerLog("导出耗时: " + str(round((time.time() - intIndexTime), 4)) + "s")
        self.logUtilObj.writerLog("==================")

        return intResult



