const API_BASE_URL = import.meta.env.VITE_SENTIMENT_API_URL;

export async function analyzeSentiment(text) {
  const response = await fetch(`${API_BASE_URL}/analyze`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text }),
  });

  if (!response.ok) {
    throw new Error(`Sentiment API error: ${response.status}`);
  }

  return response.json();
}
