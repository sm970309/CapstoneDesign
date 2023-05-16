package com.example.yeartube;


import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import org.w3c.dom.Text;

public class ResultActivity extends AppCompatActivity {
    TextView textView_title;
    TextView textView_sentence;
    TextView textView_age;
    ImageView img_age;
    TextView textView_gpt;
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.result_activity);
        img_age = findViewById(R.id.img_age);
        textView_title = findViewById(R.id.textView_title);
        textView_sentence = findViewById(R.id.textView_sentence);
        textView_age = findViewById(R.id.textView_age);
        textView_gpt = findViewById(R.id.textView_gpt);


    }
}
