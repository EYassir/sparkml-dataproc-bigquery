from google.cloud import bigquery
from google.cloud.exceptions import NotFound
# Create a new Google BigQuery client using Google Cloud Platform project
# defaults.
client = bigquery.Client()
# Prepare a reference to a new dataset for storing the query results.
dataset_id = "natality_regression"

def create_dataset():
    dataset = bigquery.Dataset(client.dataset(dataset_id))

    # Create the new BigQuery dataset.
    dataset = client.create_dataset(dataset)

    # In the new BigQuery dataset, create a reference to a new table for
    # storing the query results.
    table_ref = dataset.table("regression_input")

    # Configure the query job.
    job_config = bigquery.QueryJobConfig()

    # Set the destination table to the table reference created above.
    job_config.destination = table_ref

    # Set up a query in Standard SQL, which is the default for the BigQuery
    # Python client library.
    # The query selects the fields of interest.
    query = """
        SELECT
            weight_pounds, mother_age, father_age, gestation_weeks,
            weight_gain_pounds, apgar_5min
        FROM
            `bigquery-public-data.samples.natality`
        WHERE
            weight_pounds IS NOT NULL
            AND mother_age IS NOT NULL
            AND father_age IS NOT NULL
            AND gestation_weeks IS NOT NULL
            AND weight_gain_pounds IS NOT NULL
            AND apgar_5min IS NOT NULL
    """

    # Run the query.
    query_job = client.query(query, job_config=job_config)
    query_job.result()  # Waits for the query to finish

def delete_dataset():
    client.delete_dataset(
        dataset_id, delete_contents=True, not_found_ok=True
    )  
    print("Deleted dataset '{}'.".format(dataset_id))

# check if data set exist
try:
    client.get_dataset(dataset_id)  
    print("Dataset {} already exists".format(dataset_id))
    print("Deleting {} ".format(dataset_id))
    delete_dataset()
    create_dataset()
except NotFound:
    print("Dataset {} is not found".format(dataset_id))
    create_dataset()