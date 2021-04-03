package main

import (
    "github.com/jmoiron/sqlx"
)

type IndividualContrAgent struct {
    ID        string
    Name      string
    PhoneNumber string
    Address   string
    Description string
}

type IndividualContrAgentRepo struct {
    db *sqlx.DB
}

type IndividualContrAgentI interface {
    Create(*IndividualContrAgent) (string, error)
}

func NewIndividualContrAgent(db *sqlx.DB) IndividualContrAgentI {
    return &IndividualContrAgentRepo{
        db: db,
    }
}

func(ica *IndividualContrAgentRepo) Create(agent IndividualContrAgent) (string, error) {
    query := `INSERT INTO IndividualContrAgent (
        id, 
        name,
        phonenumber,
        address,
        description)
        values($1, $2, $3, $4, $5);`
    prp, err := ica.db.Prepare(query)

        if err != nil {
        return "", err
    }
    _, err = prp.Exec(
        agent.ID,
        agent.Name,
        agent.PhoneNumber,
        agent.Address,
        agent.Description,
    )
    if err != nil {
        return "", err
    }

    return agent.ID, err
}