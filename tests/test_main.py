import pytest

@pytest.mark.asyncio
async def test_get_person(schema):
    query = """
    query TestQuery {
        person {
            email
            name
            addresses {
                edges {
                    node {
                        street
                        state
                        number
                        city
                    }
                }
            }
        }
        }
    """
    result = await schema.execute(query)
    assert result.errors is None
    assert result.data['person'] == [
        {
            "name": "Sean",
            "email": "sean.xiang@email.com",
            "addresses": {
                "edges": [
                    {
                        "node": {
                            "street": "Main Street",
                            "state": "NSW",
                            "number": 3,
                            "city": "Sydney"
                        }
                    }
                ]
            }
        },
        {
            "name": "John",
            "email": "john.smith@email.com",
            "addresses": {
                "edges": [
                    {
                        "node": {
                            "street": "Main Street",
                            "state": "WA",
                            "number": 1,
                            "city": "Sydney"
                        }
                    },
                    {
                        "node": {
                            "street": "Main Street",
                            "state": "ACT",
                            "number": 2,
                            "city": "Sydney"
                        }
                    }
                ]
            }
        },
        {
            "name": "Jane",
            "email": "jane@email.com",
            "addresses": {
                "edges": []
            }
        }
    ]
