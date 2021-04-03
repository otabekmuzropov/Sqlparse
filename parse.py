import sqlparse

f = open("parse.sql")
go = open("struct.go", "w+")
dictiony = {
    "uuid": "string",
    "varchar": "string",
    "timestamp": "time.Time",
    "int": "int",
    "text": "string",
    "dbname": "IndividualContrAgent",
    "interface": "IndividualContrAgentI",
    "ica":"ica"
}
#package
go.write("package main\n\n")

#import
go.write("import (\n    ")
go.write('"github.com/jmoiron/sqlx"\n)\n\n')

#struct
go.write("type {0} struct {1}\n".format(dictiony["dbname"], "{"))
go.write("    ID        {}\n".format(dictiony["uuid"]))
go.write("    Name      {}\n".format(dictiony["varchar"]))
go.write("    PhoneNumber {}\n".format(dictiony["varchar"]))
go.write("    Address   {}\n".format(dictiony["varchar"]))
go.write("    Description {}\n".format(dictiony["varchar"]))
go.write("}\n\n")

#db struct
go.write("type {0}Repo struct {1}\n".format(dictiony["dbname"], "{"))
go.write("    db *sqlx.DB\n}\n\n")

#interface
go.write("type {0}I interface {1}\n".format(dictiony["dbname"], "{"))
go.write("    Create(*{0}) (string, error)\n{1}\n\n".format(dictiony["dbname"], "}"))

#newIndCountrAgent
go.write("func New{0}(db *sqlx.DB) {1} {2}\n".format(dictiony["dbname"],dictiony["interface"], "{"))
go.write("    return &{0}Repo{1}\n".format(dictiony["dbname"], "{"))
go.write("        db: db,\n    {0}\n{1}\n\n".format("}", "}"))

#create
go.write("func(ica *{2}Repo) Create(agent {0}) (string, error) {1}\n".format(dictiony["dbname"], "{", dictiony["dbname"]))
go.write("    query := `INSERT INTO {} (\n".format(dictiony["dbname"]))
go.write("        id, \n        name,\n        phonenumber,\n        address,\n")
go.write("        description)\n        values($1, $2, $3, $4, $5);`\n")
go.write("    prp, err := ica.db.Prepare(query)\n\n    ")
go.write('    if err != nil ')
go.write("{\n")
go.write('        return "", err\n')
go.write("    }\n")
go.write("    _, err = prp.Exec(\n")
go.write("        agent.ID,\n        agent.Name,\n")
go.write("        agent.PhoneNumber,\n        agent.Address,\n        agent.Description,\n    )\n")
go.write("    if err != nil {\n        ")
go.write('return "", err\n    }\n\n')
go.write("    return agent.ID, err\n}")

#get
