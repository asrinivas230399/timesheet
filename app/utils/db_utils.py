from sqlalchemy.orm import Session


def execute_query(db: Session, query_func):
    """
    Utility function to execute a query within a session.
    :param db: Database session
    :param query_func: Function that takes a session and performs a query
    :return: Result of the query
    """
    try:
        result = query_func(db)
        return result
    except Exception as e:
        db.rollback()
        raise e


def handle_transaction(db: Session, transaction_func):
    """
    Utility function to handle transactions.
    :param db: Database session
    :param transaction_func: Function that takes a session and performs a transaction
    """
    try:
        transaction_func(db)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
