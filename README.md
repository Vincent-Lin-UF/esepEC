# ESEP Extra Credit
## How to Run:

Clone the repository

```sh
git clone https://github.com/Vincent-Lin-UF/esepEC.git
```

Import ``InMemoryDB.py`` to use the database

Example in ``main.py``

Calls ``from InMemoryDB import InMemoryDB``

Use these functions:
- ``begin_transaction``: Starts a new transaction.
- ``put(key, value)``: Adds or updates a key-value pair within a transaction
- ``get(key)``: Retrieves the value associated with a key
- ``commit``: Commits the changes made in the transaction to the main store
- ``rollback``: Discards all changes made in the transaction

## Improve for official assignment
To make it an official assignment it can include things such as using real data that will have to be used using the database we have made. Moreover, having adding unit tests on the assignment could make it more official. Lastly, they can also make an interactive CLI or even GUI to make it more interesting.