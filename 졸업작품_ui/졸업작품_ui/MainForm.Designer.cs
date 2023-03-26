
namespace 졸업작품_ui
{
    partial class MainForm
    {
        /// <summary>
        /// 필수 디자이너 변수입니다.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 사용 중인 모든 리소스를 정리합니다.
        /// </summary>
        /// <param name="disposing">관리되는 리소스를 삭제해야 하면 true이고, 그렇지 않으면 false입니다.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 디자이너에서 생성한 코드

        /// <summary>
        /// 디자이너 지원에 필요한 메서드입니다. 
        /// 이 메서드의 내용을 코드 편집기로 수정하지 마세요.
        /// </summary>
        private void InitializeComponent()
        {
            this.btn_mp4Choose = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.textbox_youtubelink = new System.Windows.Forms.TextBox();
            this.btn_filteringRun = new System.Windows.Forms.Button();
            this.textbox_filename = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // btn_mp4Choose
            // 
            this.btn_mp4Choose.Location = new System.Drawing.Point(324, 33);
            this.btn_mp4Choose.Name = "btn_mp4Choose";
            this.btn_mp4Choose.Size = new System.Drawing.Size(75, 23);
            this.btn_mp4Choose.TabIndex = 0;
            this.btn_mp4Choose.Text = "영상 선택";
            this.btn_mp4Choose.UseVisualStyleBackColor = true;
            this.btn_mp4Choose.Click += new System.EventHandler(this.btn_mp4Choose_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(59, 84);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(97, 12);
            this.label2.TabIndex = 1;
            this.label2.Text = "유튜브 링크 입력";
            // 
            // textbox_youtubelink
            // 
            this.textbox_youtubelink.Location = new System.Drawing.Point(61, 99);
            this.textbox_youtubelink.Name = "textbox_youtubelink";
            this.textbox_youtubelink.Size = new System.Drawing.Size(247, 21);
            this.textbox_youtubelink.TabIndex = 2;
            // 
            // btn_filteringRun
            // 
            this.btn_filteringRun.Location = new System.Drawing.Point(61, 155);
            this.btn_filteringRun.Name = "btn_filteringRun";
            this.btn_filteringRun.Size = new System.Drawing.Size(87, 23);
            this.btn_filteringRun.TabIndex = 3;
            this.btn_filteringRun.Text = "필터링 실행";
            this.btn_filteringRun.UseVisualStyleBackColor = true;
            this.btn_filteringRun.Click += new System.EventHandler(this.btn_filteringRun_Click);
            // 
            // textbox_filename
            // 
            this.textbox_filename.BackColor = System.Drawing.SystemColors.HighlightText;
            this.textbox_filename.Location = new System.Drawing.Point(61, 35);
            this.textbox_filename.Name = "textbox_filename";
            this.textbox_filename.ReadOnly = true;
            this.textbox_filename.Size = new System.Drawing.Size(247, 21);
            this.textbox_filename.TabIndex = 4;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(59, 20);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(57, 12);
            this.label1.TabIndex = 5;
            this.label1.Text = "영상 선택";
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.textbox_filename);
            this.Controls.Add(this.btn_filteringRun);
            this.Controls.Add(this.textbox_youtubelink);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.btn_mp4Choose);
            this.Name = "MainForm";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btn_mp4Choose;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox textbox_youtubelink;
        private System.Windows.Forms.Button btn_filteringRun;
        private System.Windows.Forms.TextBox textbox_filename;
        private System.Windows.Forms.Label label1;
    }
}

