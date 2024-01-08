import matplotlib.pyplot as plt
import numpy as np
import requests
import duckdb
import pandas as pd
import math


# Fetch the latest IPFS CID from a specified URL
LATEST_IPFS_CID_URL = 'https://raw.githubusercontent.com/davidgasquez/gitcoin-grants-data-portal/main/data/IPFS_CID'
LATEST_IPFS_CID = requests.get(LATEST_IPFS_CID_URL).text.strip()

# Construct the gateway URL
GATEWAY_URL = f'https://ipfs.filebase.io/ipfs/{LATEST_IPFS_CID}/'


# Select all projects with at least $10 in direct donations in 2023
QUERY = f"""
SELECT
    projects.title AS project,
    any_value(website) AS website,
    any_value(project_twitter) AS project_twitter,
    any_value(created_at) as created_at,
    round(sum(votes.amount_usd), 0) AS amount
FROM '{GATEWAY_URL}/round_votes.parquet' AS votes,
     '{GATEWAY_URL}/rounds.parquet' AS round,
     '{GATEWAY_URL}/projects.parquet' AS projects
WHERE votes.round_id = lower(round.id)
  AND votes.project_id = projects.project_id
  AND round_start_time >= 1672531200
  AND round_end_time <= 1703980800
GROUP BY projects.title
having sum(votes.amount_usd) >= 10
order by created_at asc
"""

query_result = duckdb.sql(QUERY).df()

query_result.to_csv('2023_direct_donations_by_project.csv')
print('There are ' + str(len(query_result.index)) + ' projects with greater than $10 in direct donations in 2023')