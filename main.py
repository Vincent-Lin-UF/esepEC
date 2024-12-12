from InMemoryDB import InMemoryDB

def  main():
    db = InMemoryDB()
    try:
        # return None
        print(db.get("A"))
        # raise exception
        db.put("A", 5)
    except Exception as e:
        print(e)

    db.begin_transaction()
    db.put("A", 5)
    # None
    print(db.get("A"))
    db.put("A", 6)
    db.commit()
    # 6
    print(db.get("A")) 

    try:
        # exception
        db.commit()
    except Exception as e:
        print(e)

    try:
        # exception
        db.rollback()
    except Exception as e:
        print(e)

    # None
    print(db.get("B"))
    db.begin_transaction()
    db.put("B", 10)
    db.rollback()
    # None
    print(db.get("B"))

if __name__ == "__main__":
    main()
