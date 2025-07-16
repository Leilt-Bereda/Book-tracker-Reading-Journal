const API_URL = "http://localhost:8000";

export async function searchBooks(query) {
  const res = await fetch(`${API_URL}/books/search?q=${encodeURIComponent(query)}`);
  return res.json();
}