package com.example.yeartube;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.widget.ProgressBar;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class LoadingScreenActivity extends AppCompatActivity {

    private TextView textView;
    private ProgressBar progressBar;
    String str;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_loading_screen);

        textView = findViewById(R.id.loading_text);
        progressBar = findViewById(R.id.progress_bar);

        // MainActivity에서 전달된 텍스트 가져오기
        String text = getIntent().getStringExtra("text");
        textView.setText(text);

        String data = textView.getText().toString();




        // 로딩 화면이 유지될 시간 설정
        int LOADING_TIME = 10000; // 10초

        // 응답을 받을 때까지 로딩 화면 유지
        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                if (true) {
                    // 새로운 액티비티를 시작하고 로딩 화면 종료
                    Intent intent = new Intent(LoadingScreenActivity.this, ResultActivity.class);
                    intent.putExtra("text", str);
                    startActivity(intent);
                    finish();
                } else {
                    // 응답이 없으면 메인 화면으로 돌아감
                    finish();
                }
            }
        }, LOADING_TIME);
    }

    @Override
    public void onBackPressed() {
        // 아무런 동작도 하지 않음
    }
}