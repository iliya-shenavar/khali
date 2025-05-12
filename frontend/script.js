fetch('http://localhost:8000/api/message')
  .then(res => res.json())
  .then(data => {
    document.getElementById('message').textContent = data.message;
  })
  .catch(err => {
    document.getElementById('message').textContent = 'Failed to fetch from backend';
    console.error(err);
  });
