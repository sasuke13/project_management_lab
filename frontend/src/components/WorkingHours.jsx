import React from 'react';
import './styles.css'; 

function WorkingHours() {
  return (
    <div className="delivery-info-container">
      <h2>Графік роботи</h2>
      <div className="working-hours-details">
        <div className="working-day">
          <h3>Понеділок - П'ятниця</h3>
          <p>9:00 ранку - 6:00 вечора</p>
        </div>
        <div className="working-day">
          <h3>Субота</h3>
          <p>10:00 ранку - 3:00 вечора</p>
        </div>
        <div className="working-day">
          <h3>Неділя</h3>
          <p>Вихідний</p>
        </div>
      </div>
      <h3>Святкові та вихідні дні</h3>
      <p>У святкові та вихідні дні ми працюємо за скороченим графіком.</p>
      <p>Звертайте увагу на оголошення щодо графіку роботи в ці дні.</p>
      <h3>Обідня перерва</h3>
      <p>Обідня перерва  з 13:00 до 14:00.</p>
    </div>
  );
}

export default WorkingHours;
