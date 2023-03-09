import React, { useEffect } from "react";
import { Link } from "react-router-dom";
import { getItems } from "../../redux/reducers/items";
import { useDispatch, useSelector } from "react-redux";
import "./Home.scss";
export default function Home() {
  const items = useSelector((s) => s.items.items);
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getItems());
  }, []);
  return (
    <>
      <section className="home">
        <div className="container">
          <div className="row">
            {items.map((item, idx) => {
              return (
                <div className="col-4">
                  <div className="home__card">
                    <img className='home__card-img' src={item.image} alt="" />
                    <h2 className="home__card-title">
                      {item.title.length > 10
                        ? item.title.substr(0, 10) + "..."
                        : item.title}
                    </h2>
                    <p className="home__card-text">
                      {item.description.length === 0
                        ? "no description"
                        : item.description.length > 30
                        ? item.description.substr(0, 30) + "..."
                        : item.description}
                    </p>
                    <div className="home__button">
                      <Link to={`/product/${idx}`}>more</Link>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </section>
    </>
  );
}
