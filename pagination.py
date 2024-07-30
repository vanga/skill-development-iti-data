import requests
import json


url = "https://wabi-india-central-a-primary-api.analysis.windows.net/public/reports/querydata?synchronous=true"
headers = {
    "Origin": "https://app.powerbi.com",
    "Pragma": "no-cache",
    "Referer": "https://app.powerbi.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-PowerBI-ResourceKey": "fbae68f4-5949-4ffe-8592-53e02f7b9215",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "Content-Type": "application/json"
}
# def fetch_data(last_key=None):

noOfRows = int(input("Enter no of rows to display: "))
payload = {
    "version": "1.0.0",
    "queries": [
        {
            "Query": {
                "Commands": [
                    {
                        "SemanticQueryDataShapeCommand": {
                            "Query": {
                                "Version": 2,
                                "From": [
                                    {
                                        "Name": "d",
                                        "Entity": "Detail Report Trainee",
                                        "Type": 0
                                    },
                                    {
                                        "Name": "t",
                                        "Entity": "Trade",
                                        "Type": 0
                                    },
                                    {
                                        "Name": "s",
                                        "Entity": "State",
                                        "Type": 0
                                    },
                                    {
                                        "Name": "di",
                                        "Entity": "District",
                                        "Type": 0
                                    },
                                    {
                                        "Name": "d1",
                                        "Entity": "Date_Table",
                                        "Type": 0
                                    },
                                    {
                                        "Name": "c",
                                        "Entity": "Category",
                                        "Type": 0
                                    },
                                    {
                                        "Name": "q",
                                        "Entity": "Qualification",
                                        "Type": 0
                                    },
                                    {
                                        "Name": "i",
                                        "Entity": "ITI",
                                        "Type": 0
                                    }
                                ],
                                "Select": [
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Source": "d"
                                                }
                                            },
                                            "Property": "pkTraineeRegNumber"
                                        },
                                        "Name": "Detail Report Trainee.pkTraineeRegNumber"
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Source": "d"
                                                }
                                            },
                                            "Property": "TraineeFirstName"
                                        },
                                        "Name": "Detail Report Trainee.TraineeFirstName"
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Source": "d"
                                                }
                                            },
                                            "Property": "Gender"
                                        },
                                        "Name": "Detail Report Trainee.Gender"
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Source": "d"
                                                }
                                            },
                                            "Property": "FatherGuardianName"
                                        },
                                        "Name": "Detail Report Trainee.FatherGuardianName"
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Source": "d"
                                                }
                                            },
                                            "Property": "MotherName"
                                        },
                                        "Name": "Detail Report Trainee.MotherName"
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Source": "t"
                                                }
                                            },
                                            "Property": "Name"
                                        },
                                        "Name": "Trade.Name"
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Source": "t"
                                                }
                                            },
                                            "Property": "Course Duration"
                                        },
                                        "Name": "Trade.Course Duration",
                                        "NativeReferenceName": "Course Duration"
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Source": "s"
                                                }
                                            },
                                            "Property": "StateName"
                                        },
                                        "Name": "State.StateName"
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Source": "di"
                                                }
                                            },
                                            "Property": "DistrictName"
                                        },
                                        "Name": "District.DistrictName"
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Source": "c"
                                                }
                                            },
                                            "Property": "Category"
                                        },
                                        "Name": "Category.Category"
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Source": "q"
                                                }
                                            },
                                            "Property": "Qualification"
                                        },
                                        "Name": "Qualification.Qualification"
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Source": "t"
                                                }
                                            },
                                            "Property": "Education Stream"
                                        },
                                        "Name": "Trade.Education Stream"
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Source": "i"
                                                }
                                            },
                                            "Property": "Name"
                                        },
                                        "Name": "ITI.Name",
                                        "NativeReferenceName": "Name"
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Source": "i"
                                                }
                                            },
                                            "Property": "ITICategory"
                                        },
                                        "Name": "ITI.ITICategory"
                                    }
                                ],
                                "Where": [
                                    {
                                        "Condition": {
                                            "In": {
                                                "Expressions": [
                                                    {
                                                        "Column": {
                                                            "Expression": {
                                                                "SourceRef": {
                                                                    "Source": "d1"
                                                                }
                                                            },
                                                            "Property": "Year_Value"
                                                        }
                                                    }
                                                ],
                                                "Values": [
                                                    [
                                                        {
                                                            "Literal": {
                                                                "Value": "'2014'"
                                                            }
                                                        }
                                                    ]
                                                ]
                                            }
                                        }
                                    },
                                    {
                                        "Condition": {
                                            "In": {
                                                "Expressions": [
                                                    {
                                                        "Column": {
                                                            "Expression": {
                                                                "SourceRef": {
                                                                    "Source": "s"
                                                                }
                                                            },
                                                            "Property": "StateName"
                                                        }
                                                    }
                                                ],
                                                "Values": [
                                                    [
                                                        {
                                                            "Literal": {
                                                                "Value": "'LADAKH'"
                                                            }
                                                        }
                                                    ]
                                                ]
                                            }
                                        }
                                    },
                                    {
                                        "Condition": {
                                            "In": {
                                                "Expressions": [
                                                    {
                                                        "Column": {
                                                            "Expression": {
                                                                "SourceRef": {
                                                                    "Source": "di"
                                                                }
                                                            },
                                                            "Property": "DistrictName"
                                                        }
                                                    }
                                                ],
                                                "Values": [
                                                    [
                                                        {
                                                            "Literal": {
                                                                "Value": "'KARGIL'"
                                                            }
                                                        }
                                                    ]
                                                ]
                                            }
                                        }
                                    }
                                ],
                                "OrderBy": [
                                    {
                                        "Direction": 2,
                                        "Expression": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Source": "d"
                                                    }
                                                },
                                                "Property": "pkTraineeRegNumber"
                                            }
                                        }
                                    }
                                ]
                            },
                            "Binding": {
                                "Primary": {
                                    "Groupings": [
                                        {
                                            "Projections": [
                                                0,
                                                1,
                                                2,
                                                3,
                                                4,
                                                5,
                                                6,
                                                7,
                                                8,
                                                9,
                                                10,
                                                11,
                                                12,
                                                13
                                            ],
                                            "Subtotal": 1
                                        }
                                    ]
                                },
                                "DataReduction": {
                                    "DataVolume": 3,
                                    "Primary": {
                                        "Window": {
                                            "Count": noOfRows
                                        }
                                    }
                                },
                                "Version": 1
                            },
                            "ExecutionMetricsKind": 1
                        }
                    }
                ]
            },
            "QueryId": "",
            "ApplicationContext": {
                "DatasetId": "b26207fa-47fb-4ccb-b8bb-279e309842ee",
                "Sources": [
                    {
                        "ReportId": "5c1da8a6-ba43-4d94-b1ed-afdded7da3cb",
                        "VisualId": "ebaf64adc17e6d650202"
                    }
                ]
            }
        }
    ],
    "cancelQueries": [],
    "modelId": 548316
}
count=0
i = 0
page_data = []
page_data.append([])
maxCount= int(input("Enter no of rows to display in one page: "))
# maxCount= 10
try:
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    allData = response.json()
    while(True):
        try:
            data=allData.get('results')[0].get('result').get('data').get('dsr').get('DS')[0].get('PH')[0].get('DM0')[count]
            page_data[i].append(data)
            count+=1
            if(count%maxCount==0):
                i+=1
                page_data.append([])
        except Exception as e:
            break
except Exception as e:
    print(f"Request failed: {e}")


if page_data and not page_data[-1]:
    page_data.pop()
print(len(page_data))
for i in range(0,len(page_data)):
    print('Page'+str(i+1))
    for j in page_data[i]:
        print(j)
    print()


