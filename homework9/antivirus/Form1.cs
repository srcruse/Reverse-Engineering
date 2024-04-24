using System;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Windows.Forms;

namespace antivirus
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        readonly string[] paths = { "C:\\njRAT.exe", "C:\\njq8.exe", "C:\\Users\\User\\AppData\\Local\\Temp\\windows.exe",
            "C:\\Users\\User\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\ecc7c8c51c0850c1ec247c7fd3602f20.exe"};

        private void btnScan_Click(object sender, EventArgs e)
        {
            bool file_exists;
            string run;
            string file;
            string results;

            Process[] nj = Process.GetProcessesByName("njRAT").Concat
                (Process.GetProcessesByName("windows")).ToArray();

            run = (nj.Length != 0) ? "njRAT is currently running" : "njRAT is not running";

            file_exists = (File.Exists(paths[0]) | File.Exists(paths[1]) | File.Exists(paths[2]));
            file = (file_exists) ? "Malicious files were found on your computer" : "No malicious files were found";

            results = run + "\n" + file;

            MessageBox.Show(results, "Scan Results", MessageBoxButtons.OK, MessageBoxIcon.Warning);
        }

        private void btnRemove_Click(object sender, EventArgs e)
        {
            // check for processes; kill if found
            Process[] nj = Process.GetProcessesByName("njRAT").Concat
                (Process.GetProcessesByName("windows")).ToArray();

            if (nj.Length != 0)
            {
                foreach (Process p in nj)
                    p.Kill();
            }
            else
                MessageBox.Show("njRAT is not running", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);

            // remove copies of njRAT
            foreach (string f in paths)
            {
                if(File.Exists(f))
                    File.Delete(f);
            }
        }
    }
}
