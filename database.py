from sqlalchemy import create_engine, text
import os

db_name = "jovian_careers"
db_connection_string =  os.environ['LOCAL_DB_CONNECTION_STRING']+db_name+"?charset=utf8mb4"

engine = create_engine(db_connection_string,
                    ## FOR SSL CERTIFICATE WE NEED TO CHECK DATABASE PROVIDER 
                    #  connect_args={
                    #     "ssl": {
                    #         "ca": "/home/gord/client-ssl/ca.pem",
                    #         "cert": "/home/gord/client-ssl/client-cert.pem",
                    #         "key": "/home/gord/client-ssl/client-key.pem"
                    #     }
                    #  }
                    )

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
        
        return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text(f"SELECT * FROM jobs WHERE id = {id}")
            )
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
        
        if len(jobs):
            return jobs[0]
        else:
            return None