import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams } from "react-router-dom";
import { getProduct } from "../../redux/reducers/items";
import "./Product.scss";
export default function Product() {
  const params = useParams();
  const dispatch = useDispatch();
  const product = useSelector((s) => s.items.product);
  const navigate = useNavigate();
  useEffect(() => {
    dispatch(getProduct(params.idx));
  }, []);
  return (
    <section >
      <h2>{product.title}</h2>
      <img src={product.image} alt="" />
    </section>
  )
}
