async function sendPostRequest() {
  const url = 'http://127.0.0.1:8000/post_add_users/';
  const data = {
      name: 'Yunus',
      surname: 'Emre',
      phone: '4532169870',
      budget: 3620
  };

  const response = await fetch(url, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
  });

  if (response.ok) {
      const result = await response.json();
      console.log(result);
  } else {
      console.error('POST isteği başarısız oldu.');
  }
}