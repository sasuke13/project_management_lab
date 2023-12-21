import React from 'react';
import './styles.css'; 

function OurSuccess() {
  return (
    <div className="delivery-info-container">
      <h2>Наші успіхи</h2>
      <div className="success-details">
        <div className="success-item">
          <h3>Партнерство з великими компаніями</h3>
          <p>Ми пишаємося тим, що співпрацюємо з провідними компаніями у сфері логістики.</p>
          <img src="success4.png" alt="Success 3" style={{height:'90px', width:'400px', paddingLeft:'2%'}} />
          <img src="success5.png" alt="Success 4" style={{height:'90px', width:'400px', paddingLeft:'2%'}}/>
        </div>
        <div className="success-item">
          <h3>Ефективна система доставки</h3>
          <p>Наша ефективна система доставки забезпечує швидке та точне виконання замовлень.</p>
        </div>
        <div className="success-item">
        
          <img src="success2.jpg" alt="Success 2" style={{height:'190px', width:'290px', paddingLeft:'2%'}} />
          <img src="success3.jpg" alt="Success 1" style={{height:'190px', width:'290px', paddingLeft:'2%'}}/>
          
          <h3>Задоволені клієнти</h3>
          <p>Наша першочергова мета - задовольнені клієнти, які обирають нас знову та знову.</p>
        </div>
      </div>
      <p>Безперервне вдосконалення та великі досягнення роблять нас лідером у галузі доставки!</p>
    </div>
  );
}

export default OurSuccess;
