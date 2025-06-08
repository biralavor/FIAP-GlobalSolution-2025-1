package br.com.data4lives.sirena;

import br.com.data4lives.sirena.reports.Reporte;
import br.com.data4lives.sirena.reports.ReporteList;

public class Confiabilidade {

    private int idConfiabilidade;
    private String grauConfiabilidade;

    public Confiabilidade() {
        idConfiabilidade = 0; 
        grauConfiabilidade = "Indefinido"; 
    }
    
    public int getIdConfiabilidade() {
        return idConfiabilidade;
    }

    public void setIdConfiabilidade(int idConfiabilidade) {
        this.idConfiabilidade = idConfiabilidade;
    }

    public String getGrauConfiabilidade() {
        return grauConfiabilidade;
    }

    public void setGrauConfiabilidade(String grauConfiabilidade) {
        this.grauConfiabilidade = grauConfiabilidade;
    }

    public void calculoConfiabilidade(ReporteList reporteList) {
        Reporte[] listaReportes = reporteList.getReportes();
        for (int indice = 0; indice < reporteList.getQuantidadeReportes(); indice++) {
            Reporte reporte = listaReportes[indice];
            String localizacao = reporte.getLocalizacao().getNomeRua();
            String tipoReporte = reporte.getTipoReporte();
            String data = reporte.getData();
            int recorrencia = 0;
            for (int indiceComparador = 0; indiceComparador < reporteList.getQuantidadeReportes(); indiceComparador++) {
                Reporte comparador = listaReportes[indiceComparador];
                if (comparador.getLocalizacao().getNomeRua().equals(localizacao) && 
                    comparador.getTipoReporte().equals(tipoReporte) &&
                    comparador.getData().equals(data)) {
                    recorrencia++;
                }
            }
            // System.out.println("repeticoes: " + recorrencia);
            Confiabilidade confiabilidadeIndividual = new Confiabilidade();
            if (recorrencia < 2) {
                confiabilidadeIndividual.setGrauConfiabilidade("Baixa");
            } else if (recorrencia >= 2 && recorrencia <= 4) {
                confiabilidadeIndividual.setGrauConfiabilidade("Média");
            } else {
                confiabilidadeIndividual.setGrauConfiabilidade("Alta");
            }
            reporte.setConfiabilidade(confiabilidadeIndividual);
        }
    }
}
