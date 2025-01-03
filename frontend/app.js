document.getElementById('readingForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const date = document.getElementById('date').value;
  const count = document.getElementById('count').value;

  const response = await fetch('http://localhost:5000/log', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
      },
      body: JSON.stringify({ date, count: parseInt(count) })
  });

  if (response.ok) {
      const result = await response.json();
      console.log('Reading logged:', result);
      updateStreak();
      document.getElementById('readingForm').reset();
  }
});

async function updateStreak() {
  const response = await fetch('http://localhost:5000/streak', {
      headers: {
          'Access-Control-Allow-Origin': '*'
      }
  });
  const data = await response.json();
  document.getElementById('streak').textContent =
      `Current Streak: ${data.current_streak} days | Max Streak: ${data.max_streak} days`;
}

// Update streak on page load
updateStreak();
