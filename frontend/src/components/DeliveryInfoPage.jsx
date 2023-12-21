import React from 'react';
import './styles.css';

const DeliveryInfoPage = () => {
  return (
    <div className="delivery-info-container">
      <h2>Вартість та Інформація про Доставку</h2>

      <section className="delivery-section">
        <h3>Наші Тарифи</h3>
        <p>
          Ми пропонуємо різні тарифи доставки в залежності від ваги та відстані.
          Докладну інформацію про тарифи можна знайти на нашому веб-сайті або
          звернутися до нашої служби підтримки.
        </p>
      </section>

      <section className="pricing-section">
        <h3>Ціни за Послуги</h3>
        <ul>
          <li>
            <strong>Стандартна Доставка:</strong> $50.00
          </li><br/>
          <li>
            <strong>Експрес-Доставка:</strong> $100.00
          </li>
          <li>
            <strong>Доставка в міжнародній регіон:</strong> Залежить від відстані та ваги
          </li>
        </ul>
      </section>

      <section className="contact-section">
        <h3>Зв'яжіться з Нами <h4>0983277999</h4></h3>
        <p>
          Якщо у вас є питання щодо вартості доставки або ви хочете отримати
          індивідуальний розрахунок, будь ласка, зв'яжіться з нашою службою підтримки
          за телефоном чи електронною поштою. 
        </p>
      </section>
    </div>
  );
};

export default DeliveryInfoPage;
