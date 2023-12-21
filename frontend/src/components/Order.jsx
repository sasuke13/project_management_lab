import React from 'react';
import { Link } from 'react-router-dom'; 
import ReactDOM from "react-dom";
import './styles.css';

function Order(props) {
  const order = props?.order || {}
  
  return (
    <div className="order-container">
        <div className='order-title'>
            <h2>[ {order.id || 0} ] --- {order.title || "Unknown"}</h2>
        </div>
        <div className='order-content'>
            <div className='description-block'>
                {order.description || "Опис відсутній"}
            </div>
            <div className='price-block'>
                Ціна замовлення: {order.price || "ціна не задана"}
            </div>
        </div>
        
        
    </div>
  );
}

export default Order;
