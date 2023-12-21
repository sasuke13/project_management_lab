 const BASE_URL = process.env.REACT_APP_API_BASE_URL || 'https://your-api-endpoint.com';

export const createOrder = async (orderData) => {
  try {
    const response = await fetch(`${BASE_URL}/orders`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        // Додайте інші заголовки або токени авторизації, якщо потрібно
      },
      body: JSON.stringify(orderData),
    });

    if (!response.ok) {
      throw new Error('Failed to create order');
    }

    return response.json();
  } catch (error) {
    console.error('API Error:', error.message);
    throw error;
  }
};
