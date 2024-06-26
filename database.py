import mysql.connector
import sys


class dbhelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(user='root', password ='', host='localhost', database='Jovian_Careers')
            self.cursor = self.conn.cursor()
        except:
            print('Could not connect to database')
            sys.exit(0)
        else:
            print('Successfully connected to database')

    def fetch_data(self):
        self.cursor.execute('''
        SELECT * FROM jobs;
        ''')

        data = self.cursor.fetchall()
        return data

    def fetch_job_data(self, id):
        self.cursor.execute('''
        SELECT * FROM jobs WHERE id = {}
        '''.format(id))

        data = self.cursor.fetchall()
        print(data[0])
        return data[0]          # 0th item in the list (only item)

    def submit_application(self, job_id, applicant_details):
        query = '''
        INSERT INTO applications(job_id, name, email, education, experience, linkedin, resume) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        '''

        data = [job_id, applicant_details['name'], applicant_details['email'], applicant_details['education'], applicant_details['experience'], applicant_details['linkedin'], applicant_details['resume']]

        self.cursor.execute(query, data)
        self.conn.commit()