# TODO: add here interface tests for the requirer side
import json

from interface_tester import Tester
from scenario import State, Relation


def test_nothing_happens_if_remote_empty():
    # GIVEN that the remote end has not published any tables
    t = Tester(
        State(
            leader=True,
            relations=[
                Relation(
                    endpoint="my-fancy-database",  # the name doesn't matter
                    interface="my_fancy_database",
                )
            ],
        )
    )
    # WHEN the database charm receives a relation-joined event
    state_out = t.run("my-fancy-database-relation-joined")
    # THEN no data is published to the (local) databags
    t.assert_relation_data_empty()


def test_contract_happy_path():
    # GIVEN that the remote end has requested tables in the right format
    tables_json = json.dumps(["users", "passwords"])
    t = Tester(
        State(
            leader=True,
            relations=[
                Relation(
                    endpoint="my-fancy-database",  # the name doesn't matter
                    interface="my_fancy_database",
                    remote_app_data={"tables": tables_json},
                )
            ],
        )
    )
    # WHEN the database charm receives a relation-changed event
    state_out = t.run("my-fancy-database-relation-changed")
    # THEN the schema is satisfied (the database charm published all required fields)
    t.assert_schema_valid()
