import requests
import json
from pathlib import Path
import copy

states = [
    "ANDAMAN AND NICOBAR ISLANDS",
    "ANDHRA PRADESH",
    "ARUNACHAL PRADESH",
    "ASSAM",
    "BIHAR",
    "CHANDIGARH",
    "CHHATTISGARH",
    "DELHI",
    "GOA",
    "GUJARAT",
    "HARYANA",
    "HIMACHAL PRADESH",
    "JAMMU AND KASHMIR",
    "JHARKHAND",
    "KARNATAKA",
    "KERALA",
    "LADAKH",
    "LAKSHADWEEP",
    "MADHYA PRADESH",
    "MAHARASHTRA",
    "MANIPUR",
    "MEGHALAYA",
    "MIZORAM",
    "NAGALAND",
    "ODISHA",
    "PUDUCHERRY",
    "PUNJAB",
    "RAJASTHAN",
    "SIKKIM",
    "TAMIL NADU",
    "TELANGANA",
    "THE DADRA AND NAGAR HAVELI AND DAMAN AND DIU",
    "TRIPURA",
    "UTTAR PRADESH",
    "UTTARAKHAND",
    "WEST BENGAL",
]

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
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Content-Type": "application/json",
}
# def fetch_data(last_key=None):

noOfRows = 1000
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
                                        "Type": 0,
                                    },
                                    {"Name": "t", "Entity": "Trade", "Type": 0},
                                    {"Name": "s", "Entity": "State", "Type": 0},
                                    {"Name": "di", "Entity": "District", "Type": 0},
                                    {"Name": "d1", "Entity": "Date_Table", "Type": 0},
                                    {"Name": "c", "Entity": "Category", "Type": 0},
                                    {"Name": "q", "Entity": "Qualification", "Type": 0},
                                    {"Name": "i", "Entity": "ITI", "Type": 0},
                                ],
                                "Select": [
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {"Source": "d"}
                                            },
                                            "Property": "pkTraineeRegNumber",
                                        },
                                        "Name": "Detail Report Trainee.pkTraineeRegNumber",
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {"Source": "d"}
                                            },
                                            "Property": "TraineeFirstName",
                                        },
                                        "Name": "Detail Report Trainee.TraineeFirstName",
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {"Source": "d"}
                                            },
                                            "Property": "Gender",
                                        },
                                        "Name": "Detail Report Trainee.Gender",
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {"Source": "d"}
                                            },
                                            "Property": "FatherGuardianName",
                                        },
                                        "Name": "Detail Report Trainee.FatherGuardianName",
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {"Source": "d"}
                                            },
                                            "Property": "MotherName",
                                        },
                                        "Name": "Detail Report Trainee.MotherName",
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {"Source": "t"}
                                            },
                                            "Property": "Name",
                                        },
                                        "Name": "Trade.Name",
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {"Source": "t"}
                                            },
                                            "Property": "Course Duration",
                                        },
                                        "Name": "Trade.Course Duration",
                                        "NativeReferenceName": "Course Duration",
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {"Source": "s"}
                                            },
                                            "Property": "StateName",
                                        },
                                        "Name": "State.StateName",
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {"Source": "di"}
                                            },
                                            "Property": "DistrictName",
                                        },
                                        "Name": "District.DistrictName",
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {"Source": "c"}
                                            },
                                            "Property": "Category",
                                        },
                                        "Name": "Category.Category",
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {"Source": "q"}
                                            },
                                            "Property": "Qualification",
                                        },
                                        "Name": "Qualification.Qualification",
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {"Source": "t"}
                                            },
                                            "Property": "Education Stream",
                                        },
                                        "Name": "Trade.Education Stream",
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {"Source": "i"}
                                            },
                                            "Property": "Name",
                                        },
                                        "Name": "ITI.Name",
                                        "NativeReferenceName": "Name",
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {"Source": "i"}
                                            },
                                            "Property": "ITICategory",
                                        },
                                        "Name": "ITI.ITICategory",
                                    },
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
                                                            "Property": "Year_Value",
                                                        }
                                                    }
                                                ],
                                                "Values": [
                                                    [
                                                        {
                                                            "Literal": {
                                                                "Value": "'DUMMY_YEAR'"
                                                            }
                                                        }
                                                    ]
                                                ],
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
                                                            "Property": "StateName",
                                                        }
                                                    }
                                                ],
                                                "Values": [
                                                    [
                                                        {
                                                            "Literal": {
                                                                "Value": "'DUMMY_STATE'"
                                                            }
                                                        }
                                                    ]
                                                ],
                                            }
                                        }
                                    },
                                ],
                                "OrderBy": [
                                    {
                                        "Direction": 2,
                                        "Expression": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {"Source": "d"}
                                                },
                                                "Property": "pkTraineeRegNumber",
                                            }
                                        },
                                    }
                                ],
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
                                                13,
                                            ],
                                            "Subtotal": 1,
                                        }
                                    ]
                                },
                                "DataReduction": {
                                    "DataVolume": 3,
                                    "Primary": {"Window": {"Count": noOfRows}},
                                },
                                "Version": 1,
                            },
                            "ExecutionMetricsKind": 1,
                        }
                    }
                ]
            },
            "QueryId": "",
        }
    ],
    "cancelQueries": [],
    "modelId": 548316,
}


def fetch_data(year, state):
    current_payload = copy.deepcopy(payload)
    current_payload["queries"][0]["Query"]["Commands"][0][
        "SemanticQueryDataShapeCommand"
    ]["Query"]["Where"][0]["Condition"]["In"]["Values"][0][0]["Literal"][
        "Value"
    ] = f"'{year}'"
    current_payload["queries"][0]["Query"]["Commands"][0][
        "SemanticQueryDataShapeCommand"
    ]["Query"]["Where"][1]["Condition"]["In"]["Values"][0][0]["Literal"][
        "Value"
    ] = f"'{state}'"
    i = 0
    try:
        while True:
            output_path = Path(f"data/raw/{state}/{year}/{i}.json")
            output_path.parent.mkdir(parents=True, exist_ok=True)
            if output_path.exists():
                # read, set RT, increment i and continue
                with open(output_path) as f:
                    data = json.load(f)
                    rt = (
                        data.get("results")[0]
                        .get("result", {})
                        .get("data", {})
                        .get("dsr", {})
                        .get("DS")[0]
                        .get("RT")
                    )
                    current_payload["queries"][0]["Query"]["Commands"][0][
                        "SemanticQueryDataShapeCommand"
                    ]["Binding"]["DataReduction"]["Primary"]["Window"][
                        "RestartTokens"
                    ] = rt
                    i += 1
                    continue
            response = requests.post(
                url, headers=headers, json=current_payload, timeout=120
            )
            response.raise_for_status()
            data = response.json()
            with open(output_path, "w") as f:
                f.write(json.dumps(data))
                print(f"Data written to {output_path}")

            try:
                rt_exists = (
                    data.get("results")[0]
                    .get("result", {})
                    .get("data", {})
                    .get("dsr", {})
                    .get("DS")[0]
                    .get("RT")
                )
                if rt_exists:
                    print("next page exists")
                    i += 1
                    rt = (
                        data.get("results")[0]
                        .get("result", {})
                        .get("data", {})
                        .get("dsr", {})
                        .get("DS")[0]
                        .get("RT")
                    )
                    current_payload["queries"][0]["Query"]["Commands"][0][
                        "SemanticQueryDataShapeCommand"
                    ]["Binding"]["DataReduction"]["Primary"]["Window"][
                        "RestartTokens"
                    ] = rt
                else:
                    break
            except Exception as e:
                print(f"Request failed: {e}")
                break
    except Exception as e:
        print(f"Request failed: {e}")


for state in states:
    for year in range(2014, 2023):
        fetch_data(str(year), state)
