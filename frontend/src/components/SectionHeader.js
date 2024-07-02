import React from "react";

export default function SectionHeader(props){
    const {title} = props;
    return(
        <div className="sectionHeader text-white mt-5 pt-4">
            <h1 className="page-title text-2xl md:text-3xl font-semibold my-2 text-left">
                {title}
            </h1>
            <hr/>
        </div>
    );
}