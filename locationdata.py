urgencias = ["low", "medium", "high"]
urgencias_pesos = [0.6, 0.3, 0.1]
ubicaciones_datos = {"patio": [-1, True], "almacén": [-1, True], "comedor": [1, True], "sala sum": [1, False],
                     "entrada": [1, False], "entrada fase 2": [1, True], "counter alumnos": [1, False],
                     "counter admisión": [1, False], "auditorio": [-1, False], "aula magna": [-1, True],
                     "jardines": [6, False], "estacionamiento": [-1, False], "el café": [6, False],
                     "listo": [1, False], "lia cook": [11, False], "dirección general": [10, False]}
ubicaciones_sin_datos = ["aula", "laboratorio", "sala de estudio",
               "oficina"]


ubicaciones =  ubicaciones_sin_datos + list(ubicaciones_datos.keys())


aulas_datos = {"A101": [1, False], "A102": [1, False], "A201": [2, False], "A202": [2, False],
               "A203": [2, False],
               "M301": [3, True], "M302": [3, True], "M303": [3, True], "A401": [4, False],
               "A402": [4, False],
               "A501": [5, False], "A502": [5, False], "A601": [6, False], "A602": [6, False],
               "M601": [6, False], "M602": [6, False], "M603": [6, False], "M604": [6, False],
               "A701": [7, False], "A702": [7, False], "A703": [7, False], "A704": [7, False],
               "A705": [7, False], "A706": [7, False], "A707": [7, False], "A708": [7, False],
               "A801": [8, False], "A802": [8, False], "A803": [8, False], "A804": [8, False],
               "M801": [8, False], "M802": [8, False], "M803": [8, False], "M804": [8, False],
               "A901": [9, False], "A902": [9, False], "A903": [9, False], "A904": [9, False],
               "A905": [9, False], "A906": [9, False], "A907": [9, False], "A908": [9, False],
               "A1001": [10, False], "A1002": [10, False], "S1101": [11, False], "S1102": [11, False]
               }
laboratorios_datos = {"L101": [1, False], "L102": [1, False], "L103": [1, True], "L104": [1, True],
                      "L105": [1, True], "L106": [1, True], "L107": [1, True], "L108": [1, True],
                      "L201": [2, False], "L202": [2, False], "L203": [2, False], "L204": [2, False],
                      "L205": [2, False], "L206": [2, False], "L207": [2, True], "L208": [2, True],
                      "L209": [2, True], "L210": [2, True], "L211": [2, True], "L212": [2, True],
                      "L401": [4, False], "L402": [4, False], "L403": [4, False], "L404": [4, False], "L405": [4, False], "L406": [4, False],
                      "L407": [4, False], "L408": [4, False], "L409": [4, False], "L410": [4, False], "L411": [4, False], "L412": [4, False],
                      "L413": [4, False], "L414": [4, False], "L415": [4, False],
                      "L501": [5, False], "L502": [5, False], "L503": [5, False], "L504": [5, False],
                      "L505": [5, False], "L506": [5, False], "L507": [5, False], "L508": [5, False],
                      "L601": [6, False], "L021": [-2, False], "L022": [-2, False]
                      }
oficinas_datos = {"P201": [2, False], "P202": [2, False], "P203": [2, False], "P204": [2, False],
                  "P205": [2, False], "P206": [2, False],
                  "P207": [2, True], "P208": [2, True], "P209": [2, True], "P210": [2, True],
                  "P211": [2, True], "P212": [2, True],
                  "P301": [3, False], "P302": [3, False], "P303": [3, False], "P304": [3, False],
                  "P305": [3, False], "P306": [3, False], "P307": [3, False], "P308": [3, False],
                  "P309": [3, False], "P310": [3, False], "P311": [3, False], "P312": [3, False],
                  "P313": [3, False], "P314": [3, False], "P315": [3, False], "P316": [3, False],
                  "P317": [3, False], "P318": [3, False], "P319": [3, False], "P320": [3, False],
                  "P321": [3, True], "P322": [3, True], "P323": [3, True], "P324": [3, True],
                  "P325": [3, True], "P326": [3, True], "P327": [3, True],
                  "P501": [5, False], "P502": [5, False], "P503": [5, False], "P504": [5, False],
                  "P505": [5, False], "P506": [5, False], "P507": [5, False], "P508": [5, False],
                  "P509": [5, False], "P510": [5, False], "P511": [5, False], "P512": [5, False],
                  "P513": [5, False], "P514": [5, False], "P515": [5, False], "P516": [5, False],
                  "P517": [5, False], "P518": [5, False], "P519": [5, False], "P520": [5, False],
                  "P601": [6, False], "P602": [6, False], "P603": [6, False], "P604": [6, False],
                  "P605": [6, False], "P606": [6, False], "P607": [6, False], "P608": [6, False],
                  "P609": [6, False], "P610": [6, False], "P611": [6, False], "P612": [6, False],
                  "P613": [6, False], "P614": [6, False], "P615": [6, False], "P616": [6, False],
                  "P617": [6, False], "P618": [6, False], "P619": [6, False], "P620": [6, False]
                  }


salas_estudio_datos = {"E801": [8, False], "E802": [8, False], "E803": [8, False], "E804": [8, False],
                       "E805": [8, False], "E806": [8, False], "E807": [8, False], "E808": [8, False],
                       "E809": [8, False], "E810": [8, False], "E811": [8, False], "E812": [8, False],
                       "E813": [8, False], "E814": [8, False], "E815": [8, False], "E816": [8, False],
                       "E817": [8, False],
                       "E1001": [10, False], "E1002": [10, False], "E1003": [10, False], "E1004": [10, False],
                       "E1005": [10, False], "E1006": [10, False], "E1007": [10, False], "E1008": [10, False],
                       "E1009": [10, False], "E1010": [10, False]}

tipos = ["agresión", "comportamiento", "plagio", "discriminación", "robo"]
tipos_pesos = [0.1, 0.17, 0.7, 0.02, 0.01]
