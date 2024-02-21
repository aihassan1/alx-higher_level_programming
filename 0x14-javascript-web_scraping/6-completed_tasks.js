#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

// Function to count the number of completed tasks for a given user ID
function trueCounter(data, userid) {
  let counter = 0;
  // Loop through each item in the data
  for (const item of data) {
    // Check if the item belongs to the specified user ID and if it's completed
    if (item.userId === userid && item.completed === true) {
      counter++;
    }
  }
  // Return an object with the user ID as the key and the count as the value
  return { [userid]: counter };
}

// Make a request to the provided URL
request(url, (error, response, body) => {
  if (error) {
    // If there's an error, log it
    console.log(error);
  }

  // Parse the response body into JSON format
  const body_data = JSON.parse(body);
  // Initialize an empty object to store the results
  const users_completed_tasks = {};

  // Iterate through each item in the response body data
  for (const item of body_data) {
    // Call the true_counter function to count completed tasks for the current user ID
    const result = trueCounter(body_data, item.userId);

    // Assign the result to the users_completed_tasks object
    Object.assign(users_completed_tasks, result);
  }

  // Output the object containing the count of completed tasks for each user ID
  console.log(users_completed_tasks);
});
