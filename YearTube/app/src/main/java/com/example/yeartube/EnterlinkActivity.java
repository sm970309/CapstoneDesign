package com.example.yeartube;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

public class EnterlinkActivity extends AppCompatActivity {
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.enterlink_activity);

        EditText edit_youtube_link = (EditText) findViewById(R.id.edit_youtube_link);
        Button btn_send_link = (Button) findViewById(R.id.btn_send_link);

        btn_send_link.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {
                ProgressDialog progressDialog = new ProgressDialog(this);
                progressDialog.setMessage("로딩 중...");
                progressDialog.setCancelable(false); // 사용자가 취소할 수 없도록 설정
                progressDialog.show();
            }
        });


    }
}
