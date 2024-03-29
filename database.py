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

def add_job_to_db(data):
    with engine.connect() as conn:
        result = conn.execute(text(f"INSERT INTO jobs (title, location, salary, currency, responsibilities, requirements) VALUES ('{data['title']}', '{data['location']}', {data['salary']}, '{data['currency']}', '{data['responsibilities']}', '{data['requirements']}')"))
        
        conn.commit()

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

def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = f"""INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES ({job_id}, '{data['full_name']}', '{data['email']}', '{data['linkedin_url']}', '{data['education']}', '{data['work_experience']}', '{data['resume_url']}')"""
        conn.execute(text(query))
        conn.commit()