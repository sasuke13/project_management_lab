'use client';
import React from 'react';
import images from './images';
import ImageSlider from './ImageSlider';
import './styles.css';
import { Link } from 'react-router-dom';


function MainContent() {
    
  return (

     <main>
      <div className="container">
        <div className="row" style={{ display: 'flex', flexDirection: 'row' } }>
          <div className="col-md-3 block ">
            <div style={{textAlign:'center'}}>
             <h2>Відстежити</h2>
            </div>
                <div className="containerStyle" style={{ display: 'flex', flexDirection: 'row' } }>
                    <div className="col-9" style={{width:'70%'}}  >
                        <p><a href="/delivery">Вартість доставки</a></p>
                    </div>
                    <div className="col-3 " > 
                        <button className="rounded-button" >
                            <img src="calculator1.png" alt="calculator" width="40" height="45"  className="rounded-image"  />
                          </button>
                    </div>
                </div>
                <div className="containerStyle" style={{ display: 'flex', flexDirection: 'row' }}>
                    <div className="col-9" style={{width:'70%'}}>
                        <p><a href="/term">Термін доставки</a></p>
                    </div>
                    <div className="col-3"> 
                        <button className="rounded-button">
                            <img src="clock1.png" alt="clock" width="40" height="45"  className="rounded-image" />
                          </button>
                    </div>
                </div>
                <div className="containerStyle" style={{ display: 'flex', flexDirection: 'row' }}>
                    <div className="col-8" style={{width:'70%'}}>
                        <p><a href="/workours">Графік роботи</a>
                        </p>
                    </div>
                    <div className="col-4"> 
                        <button className="rounded-button" >
                            <img src="timer1.png" alt="timer" width="40" height="45"  className="rounded-image"  />
                          </button>
                    </div>
                </div>
                <div className="containerStyle" style={{ display: 'flex', flexDirection: 'row' }}>
                    <div className="col-8" style={{width:'70%'}}>
                        <p>
                            <Link to={"/oursuccess"}>Наші успіхи</Link>
                        </p>
                    </div>
                    <div className="col-4"> 
                        <button className="rounded-button"  >
                            <img src="my_orders1.jpg" alt="my_orders" width="40" height="45"  className="rounded-image"  />
                          </button>
                    </div>
                </div>
             </div>

          <div className="col-md-9 delivery">
            <ImageSlider images={images} />
          </div>
       </div>
    </div>
    </main>
    
)
}

export default MainContent;
